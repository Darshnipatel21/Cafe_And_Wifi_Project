from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from werkzeug.security import generate_password_hash, check_password_hash

from forms import CafeForm, RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "MYCAFEANDWIFIPROJECT"

login_manager = LoginManager()
login_manager.init_app(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)
Bootstrap5(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


class Cafes(db.Model):
    __tablename__ = 'cafe'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[String] = mapped_column(String(500), unique=True, nullable=False)
    map_url: Mapped[String] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'map_url': self.map_url,
            'img_url': self.img_url,
            'location': self.location,
            'seats': self.seats,
            'has_toilet': self.has_toilet,
            'has_wifi': self.has_wifi,
            'has_sockets': self.has_sockets,
            'can_take_calls': self.can_take_calls,
            'coffee_price': self.coffee_price
        }


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        email = request.form.get('email')
        user_db = db.session.execute(db.select(User). where(User.email == email))
        user = user_db.scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        new_user = User(
            email=request.form.get('email'),
            password=generate_password_hash(password=request.form.get('password'),method="pbkdf2",salt_length=8),
            name=request.form.get('name')
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("get_all_cafe"))
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email entered.
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('You were successfully logged in.')
            return redirect(url_for('get_all_cafe'))
        elif not user:
            flash("Your email doesn't exists.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash("Your Password is incorrect.")
            return redirect(url_for('login'))
        # elif not user:
        #     flash("Your email doesn't exists.")
        #     return redirect(url_for('login'))
    return render_template("joincommunity.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_cafe'))


@app.route('/')
def get_all_cafe():
    cafes = db.session.execute(db.select(Cafes)).scalars().all()
    cafe_dict = [cafe.to_dict() for cafe in cafes]
    return render_template("index.html", all_cafes=cafe_dict)


@app.route('/name', methods=['GET', 'POST'])
def get_all_cafes():
    query = db.session.query(Cafes)

    # Apply filters based on query parameters
    if request.args.get('location'):
        query = query.filter(Cafes.location.ilike(f"%{ request.args.get('location')}%"))
    if request.args.get('Wifi') == 'yes':
        query = query.filter(Cafes.has_wifi == True)
    if request.args.get('Toilet') == 'yes':
        query = query.filter(Cafes.has_toilet == True)
    if request.args.get('Calls') == 'yes':
        query = query.filter(Cafes.can_take_calls == True)
    if request.args.get('Socket') == 'yes':
        query = query.filter(Cafes.has_sockets == True)


    cafes = query.all()
    cafe_dict = [cafe.to_dict() for cafe in cafes]
    return render_template("index.html", all_cafes=cafe_dict)


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafes(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            seats=form.seats.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            has_sockets=form.has_sockets.data,
            can_take_calls=form.can_take_calls.data,
            coffee_price=form.coffee_price.data
        )

        db.session.add(new_cafe)
        db.session.commit()

        return redirect(url_for('get_all_cafe'))

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

import streamlit as st
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# create a model class
Base = declarative_base()               # biolerplate code
 
class Food(Base):
    __tablename__ = 'food_table'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True)
    duration = Column(Integer, default=2)
    ingredients = Column(String)
    category = Column(String(7), default='veg')
    kind = Column(String(50), default='south-indian')
    created_on = Column(Date, default=datetime.now())

    def __str__(self):
        return f'{self.title} ({self.kind})'
    
# create a database
engine = create_engine('sqlite:///food.sqlite', echo=True)  # blank database
Base.metadata.create_all(engine)                            # creates all the table

# open the database -> also bioilerplate code
def open_db():
    Session = sessionmaker(bind=engine)
    return Session()

# save data in db
def save_food(title, duration=2, ingredients='', category='veg', kind='south-indian'):
    db = open_db()      
    try:
        food = Food(title=title, duration=duration, ingredients=ingredients, category=category, kind=kind)
        db.add(food)                                            # add obj to the db
        db.commit()          
        st.success(f'Food: {title} saved successfully')                                   # save the data
    except:
        st.error(f'Please fill the form correctly')
    finally:
        db.close()                                              # close the connection

def load_all_food():
    db = open_db()
    foods = db.query(Food).all()                            # get all the data
    db.close()
    return foods

def delete_food(id):
    db = open_db()
    try:
        db.query(Food).filter(Food.id == id).delete()           # delete the data
        db.commit()
        st.success('Food deleted successfully')
    except Exception as e:
        st.error(f'Error: {e}')
    finally:
        db.close()


# ui using streamlit

st.title('Food CRUD App')

with st.form("form"):
    title = st.text_input('Title')
    duration = st.number_input('Duration in Minutes', min_value=2, max_value=24*60)
    ingredients = st.text_area('Ingredients (seperate by comma)')
    category = st.selectbox('Category', ('veg', 'non-veg'))
    kind = st.selectbox('Kind', ('south-indian', 'north-indian', 'chinese', 'italian', 'japanese','junk'))
    submit = st.form_submit_button('Submit')

if submit:
    save_food(title, duration, ingredients, category, kind)
    

st.subheader('All Food Items')

if st.checkbox("show saved data"):
    for item in load_all_food():
        st.markdown(f''' 
        ---
        ### {item.title} ({item.kind})
        - **Duration**: {item.duration} minutes
        - **Category**: {item.category}
        - **Ingredients**: {item.ingredients}
        ---
        ''')

if st.checkbox("delete a food item"):
    id = st.number_input('Enter the id of the food item to delete', value=0)
    btn = st.button('Delete')
    if id> 0 and btn:
        delete_food(id)
        st.success(f'Food item with id: {id} deleted successfully')

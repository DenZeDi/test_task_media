from sqlalchemy import create_engine
from main import df_locations

engine = create_engine('sqlite:///df_location.db', echo=False)

df_locations.to_sql(name='df_location', con=engine, index=False, if_exists='replace')



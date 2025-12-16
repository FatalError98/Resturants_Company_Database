

import psycopg2 as ps
import sqlalchemy as sql
from typing import List
from sqlalchemy import ForeignKey, String, Integer, Date, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from datetime import date, DateTime

engine = create_engine("postgresql+psycopg2://postgres:csclass25@localhost/postgres")

class Base(DeclarativeBase):
    pass

# -----------------------------------------------------------
# Me
# -----------------------------------------------------------

# Create Table
class Managers(Base):
    __tablename__ = "managers"
    
    managerID: Mapped[int] = mapped_column(Integer, primary_key=True)
    managerName: Mapped[str] = mapped_column(String(50))
    managerRole: Mapped[str] = mapped_column(String(50))
    supervise: Mapped[List["Staff"]] = relationship(back_populates="manager")
    
    def __repr__(self) -> str: 
        return f"Managers(managerID={self.managerID!r}, managerName={self.managerName!r}, managerRole={self.managerRole!r})"

class Staff(Base):
    __tablename__ = "staff"
    
    staffID: Mapped[int] = mapped_column(Integer, primary_key=True)
    staffName: Mapped[str] = mapped_column(String(50))
    staffRole: Mapped[str] = mapped_column(String(50))
    managerID: Mapped[int] = mapped_column(Integer, ForeignKey("managers.managerID"),nullable=True)
    manager: Mapped["Managers"] = relationship(back_populates="supervise")
    
    def __repr__(self) -> str: 
        return f"staff(staffID={self.staffID!r}, staffName={self.staffName!r}, staffRole={self.staffRole!r})"

Base.metadata.create_all(engine)

# INSERT DATA
with Session(engine) as session:
    managers = [
        Managers(
            managerName="Aldous De Moreno",
            managerRole="Kitchen Manager",
            supervise=[
                Staff(staffName="Sue Woolmington", staffRole="Sous Chef"),
                Staff(staffName="Fanni De Metz", staffRole="Chef"),
            ],
        ),
        Managers(
            managerName="Daniele Hallmark",
            managerRole="General Manager",
            supervise=[],
        ),
        Managers(
            managerName="Morrie Boyles",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Isis Widdop", staffRole="Bartender"),
                Staff(staffName="Scarface Smitham", staffRole="Dishwasher"),
            ],
        ),
        Managers(
            managerName="Gusty Olivet",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Palm Burdekin", staffRole="Busser"),
            ],
        ),
        Managers(
            managerName="Hartwell Douse",
            managerRole="General Manager",
            supervise=[
                Staff(staffName="Brodie Dinley", staffRole="Dishwasher"),
                Staff(staffName="Rafaela Pancoust", staffRole="Busser"),
            ],
        ),
        Managers(
            managerName="Diandra Donett",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Towny Hacking", staffRole="Dishwasher"),
                Staff(staffName="Robb Tieman", staffRole="Bartender"),
                Staff(staffName="Erinna Legrave", staffRole="Dishwasher"),
                Staff(staffName="Mike Fist", staffRole="Bartender"),
                Staff(staffName="Aldric Kauffman", staffRole="Busser"),
            ],
        ),
        Managers(
            managerName="Jareb MacGragh",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Ethel Gepp", staffRole="Server"),
                Staff(staffName="Karlene Worvill", staffRole="Dishwasher"),
                Staff(staffName="Rickey Rickert", staffRole="Server"),
            ],
        ),
        Managers(
            managerName="Mechelle Bracchi",
            managerRole="Kitchen Manager",
            supervise=[
                Staff(staffName="Arther Mila", staffRole="Sous Chef"),
                Staff(staffName="Tally Bramo", staffRole="Dishwasher")            
            ],
        ),
        Managers(
            managerName="Alyda Idenden",
            managerRole="Kitchen Manager",
            supervise=[
                Staff(staffName="Domeniga Maiden", staffRole="Chef"),
                Staff(staffName="Philis Moralis", staffRole="Busser"),
                Staff(staffName="Winny Yeld", staffRole="Host"),
                Staff(staffName="Rozanna Cousans", staffRole="Sous Chef"),
            ],
        ),
        Managers(
            managerName="Dev Bundy",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Reginauld Cowthard", staffRole="Dishwasher"),
                Staff(staffName="Jolynn Olerenshaw", staffRole="Sous Chef"),
            ],
        ),
        Managers(
            managerName="Adelheid Tubble",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Kennith Doudney", staffRole="Busser"),
                Staff(staffName="Rodger Putten", staffRole="Busser"),
            ],
        ),
        Managers(
            managerName="Kelsey Coote",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Kalvin Heersema", staffRole="Sous Chef"),
                Staff(staffName="Cammy Schaben", staffRole="Server"),
            ],
        ),
        Managers(
            managerName="Ulric Fones",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Alethea Cawthorne", staffRole="Server"),
                Staff(staffName="Nettle Gregson", staffRole="Busser"),
            ],
        ),
        Managers(
            managerName="Connie Willmer",
            managerRole="Floor Manager",
            supervise=[],
        ),
        Managers(
            managerName="Mellicent Maddern",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Inna Clout", staffRole="Dishwasher"),
                Staff(staffName="Sherman Mongin", staffRole="Bartender"),
                Staff(staffName="Norbert De Bellis", staffRole="Server"),
            ],
        ),
        Managers(
            managerName="Amil Karys",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Jorrie Bowmer", staffRole="Chef"),
                Staff(staffName="Bekki Di Domenico", staffRole="Server"),
                Staff(staffName="Anselm Megarrell", staffRole="Bartender"),
            ],
        ),
        Managers(
            managerName="Emmett Bartosik",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Tammi Grivori", staffRole="Bartender"),
            ],
        ),
        Managers(
            managerName="Mikey Riccelli",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Killian Micklewicz", staffRole="Busser"),
                Staff(staffName="Philip Chapling", staffRole="Server"),
                Staff(staffName="Gill Jobb", staffRole="Host"),
                Staff(staffName="Kym Doone", staffRole="Busser"),
                Staff(staffName="Richart Haken", staffRole="Dishwasher"),
            ],
        ),
        Managers(
            managerName="Rich Tedahl",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Murvyn Lebell", staffRole="Bartender"),
                Staff(staffName="Dael Friskey", staffRole="Dishwasher"),
                Staff(staffName="Garrick Gillyatt", staffRole="Busser"),
            ],
        ),
        Managers(
            managerName="Ruby Korda",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Gabi MacGoun", staffRole="Dishwasher"),
            ],
        ),
        Managers(
            managerName="Barbara Huish",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Justus McMorran", staffRole="Bartender"),
                Staff(staffName="Bram Baudain", staffRole="Dishwasher"),
                Staff(staffName="Sloane Simms", staffRole="Busser"),
            ],
        ),
        Managers(
            managerName="Wendy MacGahey",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Alvie Lyst", staffRole="Busser"),
            ],
        ),
        Managers(
            managerName="Pier Eberz",
            managerRole="Kitchen Manager",
            supervise=[
                Staff(staffName="Cari Wavell", staffRole="Chef"),
                Staff(staffName="Giselbert Galler", staffRole="Sous Chef"),
                Staff(staffName="Dulcine Gaskin", staffRole="Dishwasher"),
            ],
        ),
        Managers(
            managerName="Esther Dinnis",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Margo Tethacot", staffRole="Bartender"),
                Staff(staffName="Jami Fateley", staffRole="Server"),
            ],
        ),
        Managers(
            managerName="Izak Gogerty",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Joice Aspinal", staffRole="Server"),
            ],
        ),
        Managers(
            managerName="Hewet Goodright",
            managerRole="Floor Manager",
            supervise=[],
        ),
        Managers(
            managerName="Gaby Langdale",
            managerRole="General Manager",
            supervise=[
                Staff(staffName="Anita Richings", staffRole="Bartender"),
                Staff(staffName="Beret Haythornthwaite", staffRole="Dishwasher"),
                Staff(staffName="Delphinia Pedrocchi", staffRole="Busser"),
                Staff(staffName="Dolorita Petren", staffRole="Dishwasher"),
                Staff(staffName="Julia Thow", staffRole="Dishwasher"),
            ],
        ),
        Managers(
            managerName="Floria Frigout",
            managerRole="General Manager",
            supervise=[
                Staff(staffName="Ode Bearman", staffRole="Busser"),
            ],
        ),
        Managers(
            managerName="Cathrin Carlino",
            managerRole="General Manager",
            supervise=[
                Staff(staffName="Elbertine Goutcher", staffRole="Server"),
                Staff(staffName="Anselma Kuhndel", staffRole="Sous Chef"),
                Staff(staffName="Jayme McDonogh", staffRole="Bartender"),
            ],
        ),
        Managers(
            managerName="Eugene Treher",
            managerRole="Floor Manager",
            supervise=[
                Staff(staffName="Marshall Boothe", staffRole="Server"),
                Staff(staffName="Meryl Dredge", staffRole="Bartender"),
                Staff(staffName="Rriocard Jedrzej", staffRole="Bartender"),
            ],
        ),
    ]
    session.add_all(managers)
    session.commit()

# QUERIES
session = Session(engine)
session.query()

schema = (
    select(Staff)
    .join(Staff.manager)
    .where((Staff.staffRole == "Sous Chef") | (Staff.staffRole == "Chef"))
    .where(Managers.managerRole != "Floor Manager")
)

result = session.scalars(schema).all()

for s in result:
    print(s.staffName, "Managed by:", s.manager.managerName)


# -----------------------------------------------------------
# Team member 1
# -----------------------------------------------------------

# CREATE TABLES
class Warehouse(Base):
    __tablename__ = "warehouse"

    warehouseID: Mapped[int] = mapped_column(Integer, primary_key=True)
    warehouseLocation: Mapped[str] = mapped_column(String(100))
    warehouseItem: Mapped[str] = mapped_column(String(100))
    warehouseQty: Mapped[int] = mapped_column(Integer)

    supply: Mapped[List["Supplier"]] = relationship(back_populates="warehouse")

    def __repr__(self) -> str:
        return (f"Warehouse(warehouseID={self.warehouseID!r}, "
            f"warehouseLocation={self.warehouseLocation!r}, "
            f"warehouseItem={self.warehouseItem!r}, "
            f"warehouseQty={self.warehouseQty!r})")


class Supplier(Base):
    __tablename__ = "supplier"

    supplierID: Mapped[int] = mapped_column(Integer, primary_key=True)
    supplierName: Mapped[str] = mapped_column(String(100))
    supplierRep: Mapped[str] = mapped_column(String(100))
    supplierContact: Mapped[str] = mapped_column(String(200))

    warehouseID: Mapped[int] = mapped_column(
        Integer, ForeignKey("warehouse.warehouseID"), nullable=True)

    warehouse: Mapped["Warehouse"] = relationship(back_populates="supply")

    def __repr__(self) -> str:
        return (
            f"Supplier(supplierID={self.supplierID!r}, "
            f"supplierName={self.supplierName!r}, "
            f"supplierRep={self.supplierRep!r}, "
            f"supplierContact={self.supplierContact!r})")

Base.metadata.create_all(engine)

# INSERT DATA

with Session(engine) as session:
    warehouses = [
        Warehouse(
            warehouseLocation="New York Distribution Hub",
            warehouseItem="Fresh Produce",
            warehouseQty=3200,
            supply=[
                Supplier(
                    supplierName="GreenLeaf Farms",
                    supplierRep="Walter White",
                    supplierContact="212-555-1023"
                ),
                Supplier(
                    supplierName="Empire Organic Co.",
                    supplierRep="Jesse Pinkman",
                    supplierContact="212-555-4490"
                ),
            ],
        ),
        Warehouse(
            warehouseLocation="Los Angeles Cold Storage",
            warehouseItem="Dairy Products",
            warehouseQty=2100,
            supply=[
                Supplier(
                    supplierName="Pacific Dairy Group",
                    supplierRep="Harry Potter",
                    supplierContact="310-555-3344"
                ),
                Supplier(
                    supplierName="Sunset Creamery",
                    supplierRep="Ron Swanson",
                    supplierContact="310-555-9102"
                ),
            ],
        ),
        Warehouse(
            warehouseLocation="Chicago Dry Goods Center",
            warehouseItem="Grains & Baking Supplies",
            warehouseQty=4800,
            supply=[
                Supplier(
                    supplierName="Midwest Flour Mills",
                    supplierRep="Michael Scoot",
                    supplierContact="773-555-2781"
                ),
                Supplier(
                    supplierName="Heartland Grain Co.",
                    supplierRep="Robert Whittaker",
                    supplierContact="773-555-6632"
                ),
                Supplier(
                    supplierName="Baker’s Choice Ingredients",
                    supplierRep="Jon Jones",
                    supplierContact="773-555-9022"
                ),
            ],
        ),
        Warehouse(
            warehouseLocation="Houston Refrigerated Hub",
            warehouseItem="Meat & Poultry",
            warehouseQty=5600,
            supply=[
                Supplier(
                    supplierName="Texas Prime Meats",
                    supplierRep="Craig Jones",
                    supplierContact="832-555-7781"
                ),
                Supplier(
                    supplierName="LoneStar Poultry Co.",
                    supplierRep="Sean Brady",
                    supplierContact="832-555-2240"
                ),
            ],
        ),
        Warehouse(
            warehouseLocation="Seattle Coastal Storage",
            warehouseItem="Seafood Products",
            warehouseQty=1900,
            supply=[
                Supplier(
                    supplierName="Pacific Wave Fisheries",
                    supplierRep="Leon Edwards",
                    supplierContact="206-555-7711"
                ),
                Supplier(
                    supplierName="Northern Harbor Seafood",
                    supplierRep="Patrick Kane",
                    supplierContact="206-555-4890"
                ),
            ],
        ),
        Warehouse(
            warehouseLocation="Miami Specialty Storage",
            warehouseItem="Tropical Fruits",
            warehouseQty=2600,
            supply=[
                Supplier(
                    supplierName="Caribe Fresh Importers",
                    supplierRep="Caleb Williams",
                    supplierContact="305-555-8821"
                ),
                Supplier(
                    supplierName="SunBurst Produce Co.",
                    supplierRep="John Robertson",
                    supplierContact="305-555-7410"
                ),
            ],
        ),
    ]

    session.add_all(warehouses)
    session.commit()

# QUERY
session = Session(engine)
session.query()

with Session(engine) as session:
    results = (
        session.query(
            Warehouse.warehouseLocation,
            Warehouse.warehouseItem,
            Supplier.supplierName,
            Supplier.supplierRep,
            Warehouse.warehouseQty,
        ).join(Warehouse.supply).limit(12).all())

for row in results:
    print(row)

# -----------------------------------------------------------
# Team Member 2
# -----------------------------------------------------------

class Subsidiary(Base):
    __tablename__ = "subsidiary_ORM"

    subsidiaryID: Mapped[int] = mapped_column(Integer, primary_key = True)
    subsidiaryName: Mapped[str] = mapped_column(String(100))
    subsidiaryLocation: Mapped[str] = mapped_column(String(100))
    subsidiaryExec: Mapped[str] = mapped_column(String(100))
    execSalary: Mapped[int] = mapped_column(Integer)

    __table_args__ = (
        CheckConstraint('"execSalary" > 0', name="check_execSalary_pos"),
    )
    restaurants: Mapped[List["Restaurant"]] = relationship(
        back_populates = "subsidiary",
        cascade = "all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(subsidiaryID={self.subsidiaryID!r}, subsidiaryName={self.subsidiaryName!r}, subsidiaryLocation={self.subsidiaryLocation!r}, subsidiaryExec={self.subsidiaryExec!r}, execSalary={self.execSalary!r})"

class Restaurant(Base):
    __tablename__ = "restaurant_ORM"

    restaurantID: Mapped[int] = mapped_column(Integer, primary_key = True)
    restaurantName: Mapped[str] = mapped_column(String(100))
    restaurantLocation: Mapped[str] = mapped_column(String(100))
    restaurantType: Mapped[str] = mapped_column(String(50))
    openingDate: Mapped[str] = mapped_column(DateTime)
    subsidiaryID: Mapped[int] = mapped_column(Integer, ForeignKey("subsidiary_ORM.subsidiaryID"))
    subsidiary: Mapped["Subsidiary"] = relationship(back_populates = "restaurants")

    def __repr__(self) -> str:
        return f"User(restaurantID={self.restaurantID!r}, restaurantName={self.restaurantName!r}, restaurantLocation={self.restaurantLocation!r}, restaurantType={self.restaurantType!r}, openingDate={self.openingDate!r})"

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# INSERT DATA
# Inserting data
with Session(engine) as session:
    subsidiaries = [
    Subsidiary(
        subsidiaryID=1, subsidiaryName="North Dining Group",
        subsidiaryLocation="Chicago, IL", subsidiaryExec="Oliver Schramm",
        execSalary=180000, restaurants=[
            Restaurant(restaurantID=1, restaurantName="The North Fork",
                       restaurantLocation="Chicago, IL", restaurantType="American",
                       openingDate=date(2020,4,15), subsidiaryID=1),
            Restaurant(restaurantID=2, restaurantName="Skyline Sushi",
                       restaurantLocation="Naperville, IL", restaurantType="Japanese",
                       openingDate=date(2022,2,10), subsidiaryID=1)]
    ),
    Subsidiary(
        subsidiaryID=2, subsidiaryName="East Eats Company",
        subsidiaryLocation="New York, NY", subsidiaryExec="August Decz",
        execSalary=175000, restaurants=[
            Restaurant(restaurantID=3, restaurantName="Harbor Tap",
                       restaurantLocation="Brooklyn, NY", restaurantType="Pub",
                       openingDate=date(2018,9,12), subsidiaryID=2),
            Restaurant(restaurantID=4, restaurantName="Times Table",
                       restaurantLocation="Queens, NY", restaurantType="Italian",
                       openingDate=date(2022,6,22), subsidiaryID=2)]
    ),
    Subsidiary(
        subsidiaryID=3, subsidiaryName="South Food Incorporated",
        subsidiaryLocation="Dallas, TX", subsidiaryExec="Tom Papka",
        execSalary=172000, restaurants=[
            Restaurant(restaurantID=5, restaurantName="Southern Spoon",
                       restaurantLocation="Dallas, TX", restaurantType="BBQ",
                       openingDate=date(2020,1,18), subsidiaryID=3),
            Restaurant(restaurantID=6, restaurantName="Texan Table",
                       restaurantLocation="Austin, TX", restaurantType="Steakhouse",
                       openingDate=date(2022,3,25), subsidiaryID=3)]
    ),
    Subsidiary(
        subsidiaryID=4, subsidiaryName="West Flavor LLC",
        subsidiaryLocation="Los Angeles, CA", subsidiaryExec="Ammar Al-Zuhairi",
        execSalary=185000, restaurants=[
            Restaurant(restaurantID=7, restaurantName="Golden Coast",
                       restaurantLocation="Los Angeles, CA", restaurantType="Seafood",
                       openingDate=date(2020,2,2), subsidiaryID=4),
            Restaurant(restaurantID=8, restaurantName="Palm Grove",
                       restaurantLocation="Palm Springs, CA", restaurantType="Mediterranean",
                       openingDate=date(2023,1,20), subsidiaryID=4)]
    ),
    Subsidiary(
        subsidiaryID=5, subsidiaryName="Capital Dining and Entertainment",
        subsidiaryLocation="Washington, D.C.", subsidiaryExec="Bernie Sanders",
        execSalary=175000, restaurants=[
            Restaurant(restaurantID=9, restaurantName="Chesapeake Catch",
                       restaurantLocation="Chesapeake Bay, MD", restaurantType="Seafood",
                       openingDate=date(2023,4,18), subsidiaryID=5),
            Restaurant(restaurantID=10, restaurantName="The District",
                       restaurantLocation="Washington, D.C.", restaurantType="Steakhouse",
                       openingDate=date(2024,9,2), subsidiaryID=5)]
    )
]
## Adding my tables
session.add_all(subsidiaries)
session.commit()

# QUERY
session = Session(engine)
stmt = (
    select(Restaurant.restaurantName, Subsidiary.subsidiaryName, Restaurant.restaurantLocation)
    .join(Restaurant.subsidiary)
)
for rest, sub, rloc in session.execute(stmt):
    print(f"{rest} is based in {rloc} and is owned and operated by {sub}")

# -----------------------------------------------------------
# Team Member 3
# -----------------------------------------------------------

# Create Tables
class Restaurant(Base):
    __tablename__ = "Restaurant"

    restaurantID: Mapped[int] = mapped_column(Integer, primary_key=True)
    restaurantName: Mapped[str] = mapped_column(String(100))
    restaurantLocation: Mapped[str] = mapped_column(String(100))
    restaurantType: Mapped[str] = mapped_column(String(50))
    openingDate: Mapped[date] = mapped_column(Date)
    # 1:N relationship with Staff
    staff: Mapped[List["Staff"]] = relationship(
        back_populates="restaurant",
        cascade="all, delete-orphan"
    )
        # restaurant table missing FKs subsidiaryID and managerID bc no tables created yet
class Staff(Base):
    __tablename__ = "Staff"

    staffID: Mapped[int] = mapped_column(Integer, primary_key=True)
    staffName: Mapped[str] = mapped_column(String(100))
    staffRole: Mapped[str] = mapped_column(String(50))
    
    restaurantID: Mapped[int] = mapped_column(ForeignKey("Restaurant.restaurantID"))

    restaurant: Mapped["Restaurant"] = relationship(back_populates="staff")
        # missing FK managerID bc no table created yet 

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# INSERT DATA
restaurants = [
    Restaurant(
        restaurantID=1, restaurantName="North Fork",
        restaurantLocation="Chicago, IL", restaurantType="American",
        openingDate=date(2020,4,15)
    ),
    Restaurant(
        restaurantID=2, restaurantName="Skyline Sushi",
        restaurantLocation="Naperville, IL", restaurantType="Japanese",
        openingDate=date(2022,2,10)
    ),
    Restaurant(
        restaurantID=3, restaurantName="Urban Hearth",
        restaurantLocation="Milwaukee, WI", restaurantType="Fusion",
        openingDate=date(2023,6,12)
    ),
    Restaurant(
        restaurantID=4, restaurantName="Golden Coast",
        restaurantLocation="Los Angeles, CA", restaurantType="Seafood",
        openingDate=date(2020,2,2)
    ),
]

staff_members = [
    Staff(staffID=1, staffName="Sabrina Carpenter", staffRole="Server", restaurantID=1),
    Staff(staffID=2, staffName="Denzel Clarke", staffRole="Chef", restaurantID=1),
    Staff(staffID=3, staffName="Maya Moore", staffRole="Sous Chef", restaurantID=1),
    Staff(staffID=4, staffName="Aiden Hutchinson", staffRole="Host", restaurantID=1),
    Staff(staffID=5, staffName="Lily Allen", staffRole="Bartender", restaurantID=1),

    Staff(staffID=6, staffName="Miles Teller", staffRole="Busser", restaurantID=2),
    Staff(staffID=7, staffName="Will Toledo", staffRole="Dishwasher", restaurantID=2),
    Staff(staffID=8, staffName="Elizabeth Klings", staffRole="Server", restaurantID=2),
    Staff(staffID=9, staffName="Oprah Winfrey", staffRole="Server", restaurantID=2),
    Staff(staffID=10, staffName="Lionel Messi", staffRole="Chef", restaurantID=2),

    Staff(staffID=11, staffName="Priyanka Chopra", staffRole="Sous Chef", restaurantID=3),
    Staff(staffID=12, staffName="Ezra Koenig", staffRole="Host", restaurantID=3),
    Staff(staffID=13, staffName="Calvin Harris", staffRole="Bartender", restaurantID=3),
    Staff(staffID=14, staffName="Lana Del Rey", staffRole="Busser", restaurantID=3),
    Staff(staffID=15, staffName="Trevor May", staffRole="Dishwasher", restaurantID=3),

    Staff(staffID=16, staffName="Jennifer Lopez", staffRole="Busser", restaurantID=4),
    Staff(staffID=17, staffName="Tina Turner", staffRole="Server", restaurantID=4),
    Staff(staffID=18, staffName="Cole Swindell", staffRole="Chef", restaurantID=4),
    Staff(staffID=19, staffName="Frida Kahlo", staffRole="Sous Chef", restaurantID=4),
    Staff(staffID=20, staffName="Gordon Ramsay", staffRole="Host", restaurantID=4),
]

with Session(engine) as session:
    session.add_all(restaurants)
    session.add_all(staff_members)
    session.commit()

# QUERIES
session = Session(engine)

print("\n## JOIN: Staff with Restaurant Names ##")
stmt = (
    select(Restaurant.restaurantName, Staff.staffName, Staff.staffRole)
    .join(Staff, Staff.restaurantID == Restaurant.restaurantID)
)
for rname, sname, role in session.execute(stmt):
    print(f"{sname} works as {role} at {rname}")



brt611

make a schema class first when making a collection
look at custom entry for reference

ownshipSpeed
timestamp, speed (up to 4 digits), tactical basis
long, double, string

speed very similar to depth

copy paste another file
speed.js
connect to database
create collection
$jsonSchema

createTime: {
    bsonType: "long",
    description: "Time when created"
}

THAT'S THE SCHEMA IN THE DB

check in mongoDBcompass

once schema is finished, start kirby

niwc.pac.brtdb.collection
ownshipSpeed.java

createindex function not needed, but will speed up things for later

CollectionNames.java should have a new one called
    public static final String OWNSHIP_SPEED = "ownshipSpeed"

CollectionFields.java should have a new variables called
    public static final String OWNSHIPSPEED_SPEED = "speed"
    public static final String OWNSHIPSPEED_CREATE_TIME = "create time"
    public static final String OWNSHIPSPEED_TACTICAL_BASIS = "tactical basis"
    public static final String OWNSHIPSPEED_IS_SUNDOWN = BRT_COLLECTIONS_IS_SUNDOWN
    ...

OwnshipSpeed.java
public class OwnshipSpeed extends BrtCollections {

    setter getter field

    (NO VOID, because it causes a lot of data transfers in and out)
    public OwnshipSpeed setSpeed(double param) {
        this.speed = param
        return this
    }

    public double getSpeed() {
        return speed
    }

    MongoCollection coll = dbrmgr.getMongoDatabase().getCollection(CollectionNames.OWNSHIP_SPEED)

    create method

    read method

}

BrtMongo.java (is in Warran's own thing called brt-demo)
can be used to test the different collections, similar to like console.logging in the frontend (test crud)
OwnshipSpeed os = new OwnshipSpeed();
os.setDifferent(stuff);
...

String osId = os.create(ActiveDbMgr)
saves to the database

if (osId != null) {
    this means that theosId succuesffuly created an enetry in the database
}
DROP TABLE IF EXISTS vehicledetails;

CREATE TABLE vehicledetails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ownername VARCHAR NOT NULL,
    carnumber VARCHAR NOT NULL,
    email VARCHAR NOT NULL
);

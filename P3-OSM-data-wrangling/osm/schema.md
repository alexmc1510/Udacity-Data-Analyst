nodes

CREATE TABLE nodes(id INTEGER PRIMARY KEY, lat REAL, lon REAL, user TEXT, uid INTEGER, version INTEGER, changeset INTEGER, timestamp DATETIME);

nodes_tags

CREATE TABLE nodes_tags(id INTEGER, key TEXT, value TEXT, type TEXT, FOREIGN KEY (id) REFERENCES Nodes (id));

ways

CREATE TABLE ways(id INTEGER PRIMARY KEY, user TEXT, uid INTEGER, version INTEGER, changeset INTEGER, timestamp DATETIME);

ways_nodes

CREATE TABLE ways_nodes(id INTEGER, node_id INTEGER, position INTEGER, FOREIGN KEY(id) REFERENCES Nodes(id));

ways_tags

CREATE TABLE ways_tags(id INTEGER, key TEXT, value TEXT, type TEXT, FOREIGN KEY(id) REFERENCES Ways(id));


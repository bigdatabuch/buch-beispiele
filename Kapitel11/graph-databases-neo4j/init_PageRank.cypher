// Alle bestehenden Daten löschen (optional)
MATCH (n) DETACH DELETE n;

// Personen und Beziehungen erstellen
CREATE
              (anna:Person {name: "Anna"}),
              (dora:Person {name: "Dora"}),
              (christin:Person {name: "Christin"}),
              (bob:Person {name: "Bob"}),
              (bernd:Person {name: "Bernd"}),
              (alice:Person {name: "Alice"}),
              (lukas:Person {name: "Lukas"}),
              (anna)-[:FRIENDS_WITH]->(bob),
              (dora)-[:FRIENDS_WITH]->(christin),
              (christin)-[:FRIENDS_WITH]->(bob),
              (bob)-[:FRIENDS_WITH]->(alice),
              (bernd)-[:FRIENDS_WITH]->(alice),
              (bernd)-[:FRIENDS_WITH]->(christin),
              (alice)-[:FRIENDS_WITH]->(bob),
              (anna)-[:FRIENDS_WITH]->(lukas),
              (anna)-[:FRIENDS_WITH]->(dora),
              (anna)-[:FRIENDS_WITH]->(alice),
              (lukas)-[:FRIENDS_WITH]->(alice);


// GDS Graph Projection erstellen
CALL gds.graph.project(
  'friends-graph',
  'Person',
  'FRIENDS_WITH'
);

// Page Rank aufrufen
CALL gds.pageRank.stream('friends-graph')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS person, score
ORDER BY score DESC;
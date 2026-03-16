CREATE
  (alice:Person {name: "Alice"}),
  (bob:Person {name: "Bob"}),
  (carol:Person {name: "Carol"}),
  (dave:Person {name: "Dave"}),
  (emma:Person {name: "Emma"}),
  (frank:Person {name: "Frank"}),
  (grace:Person {name: "Grace"}),
  (heidi:Person {name: "Heidi"}),
  (ivan:Person {name: "Ivan"}),
  (judy:Person {name: "Judy"}),
  (mallory:Person {name: "Mallory"}),
  (oscar:Person {name: "Oscar"}),
  (peggy:Person {name: "Peggy"}),

  (matrix:Movie {title: "The Matrix"}),
  (inception:Movie {title: "Inception"}),
  (godfather:Movie {title: "The Godfather"}),
  (interstellar:Movie {title: "Interstellar"}),
  (bladeRunner:Movie {title: "Blade Runner 2049"}),
  (pulpFiction:Movie {title: "Pulp Fiction"}),
  (potter:Movie {title: "Harry Potter"}),
  (darkKnight:Movie {title: "The Dark Knight"}),
  (shawshank:Movie {title: "The Shawshank Redemption"}),
  (parasite:Movie {title: "Parasite"}),
  (gladiator:Movie {title: "Gladiator"}),
  (titanic:Movie {title: "Titanic"}),
  (forrestGump:Movie {title: "Forrest Gump"}),

  (scifi:Genre {name: "Sci-Fi"}),
  (crime:Genre {name: "Crime"}),
  (drama:Genre {name: "Drama"}),
  (action:Genre {name: "Action"}),
  (thriller:Genre {name: "Thriller"}),
  (romance:Genre {name: "Romance"}),

  (alice)-[:FRIENDS_WITH]->(carol),
  (bob)-[:FRIENDS_WITH]->(dave),
  (emma)-[:FRIENDS_WITH]->(grace),
  (heidi)-[:FRIENDS_WITH]->(ivan),
  (judy)-[:FRIENDS_WITH]->(mallory),
  (oscar)-[:FRIENDS_WITH]->(peggy),

  (alice)-[:RATED {score:5}]->(matrix),
  (alice)-[:RATED {score:4}]->(inception),
  (alice)-[:RATED {score:5}]->(interstellar),

  (bob)-[:RATED {score:5}]->(godfather),
  (bob)-[:RATED {score:4}]->(pulpFiction),
  (bob)-[:RATED {score:4}]->(darkKnight),

  (carol)-[:RATED {score:4}]->(matrix),
  (carol)-[:RATED {score:5}]->(godfather),
  (carol)-[:RATED {score:4}]->(potter),

  (dave)-[:RATED {score:5}]->(interstellar),
  (dave)-[:RATED {score:4}]->(bladeRunner),

  (emma)-[:RATED {score:5}]->(parasite),
  (emma)-[:RATED {score:4}]->(shawshank),

  (frank)-[:RATED {score:5}]->(pulpFiction),
  (frank)-[:RATED {score:4}]->(potter),

  (grace)-[:RATED {score:5}]->(darkKnight),
  (grace)-[:RATED {score:4}]->(gladiator),

  (heidi)-[:RATED {score:5}]->(titanic),
  (heidi)-[:RATED {score:4}]->(forrestGump),

  (ivan)-[:RATED {score:4}]->(interstellar),
  (ivan)-[:RATED {score:5}]->(matrix),

  (judy)-[:RATED {score:5}]->(parasite),
  (judy)-[:RATED {score:4}]->(shawshank),

  (mallory)-[:RATED {score:4}]->(gladiator),
  (mallory)-[:RATED {score:5}]->(darkKnight),

  (oscar)-[:RATED {score:5}]->(forrestGump),
  (peggy)-[:RATED {score:4}]->(titanic),

  (matrix)-[:IN_GENRE]->(scifi),
  (inception)-[:IN_GENRE]->(scifi),
  (interstellar)-[:IN_GENRE]->(scifi),
  (bladeRunner)-[:IN_GENRE]->(scifi),
  (potter)-[:IN_GENRE]->(scifi), 	

  (godfather)-[:IN_GENRE]->(crime),
  (pulpFiction)-[:IN_GENRE]->(crime),

  (shawshank)-[:IN_GENRE]->(drama),
  (forrestGump)-[:IN_GENRE]->(drama),

  (darkKnight)-[:IN_GENRE]->(action),
  (gladiator)-[:IN_GENRE]->(action),

  (parasite)-[:IN_GENRE]->(thriller),
  (titanic)-[:IN_GENRE]->(romance);

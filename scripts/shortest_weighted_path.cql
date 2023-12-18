//Finds a variable length path of type “FACULTY” between a user-inputted starting and end node where all
//intermediary edges have the “Gender” attribute as “M”, the “Rank” as “Assoc” and this resultant path is also the
//one that minimizes the sum of the rank changes as one traverses the path (smallest magnitude of the sum of all in the
//path).

MATCH paths = allShortestPaths((s:Node {name: "University of Regina"}) - [rels:FACULTY*]->(e:Node{name: "Cornell University"}))
WHERE ALL(rel IN relationships(paths) WHERE rel.Gender = "M" and rel.Rank = "Assoc")
WITH paths,
     reduce(totalDelta = 0.00, rel in relationships(paths) | totalDelta + abs (rel.delta_pi)) AS totalDeltaSum
RETURN paths, totalDeltaSum
ORDER BY totalDeltaSum ASC 
LIMIT 1;

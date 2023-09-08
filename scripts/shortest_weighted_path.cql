MATCH paths = allShortestPaths((s:Node {name: "University of Regina"}) - [rels:FACULTY*]->(e:Node{name: "Cornell University"}))
WHERE ALL(rel IN relationships(paths) WHERE rel.Gender = "M" and rel.Rank = "Assoc")
WITH paths,
     reduce(totalDelta = 0.00, rel in relationships(paths) | totalDelta + abs (rel.delta_pi)) AS totalDeltaSum
RETURN paths, totalDeltaSum
ORDER BY totalDeltaSum ASC 
LIMIT 1;
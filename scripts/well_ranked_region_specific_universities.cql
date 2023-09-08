MATCH (start:Node {name: "Memorial University of Newfoundland"})
WITH start 
MATCH (end:Node {region:start.region})
WHERE end.pi is NOT NULL
WITH start,end
ORDER BY end.pi DESC
LIMIT 7
MATCH shortestPath = shortestPath((start)-[:FACULTY*]->(end))
WHERE ALL(node IN nodes(shortestPath)[1..-1] WHERE node.region = start.region)
RETURN start, nodes(shortestPath)[1..-1] AS intermediaries, end
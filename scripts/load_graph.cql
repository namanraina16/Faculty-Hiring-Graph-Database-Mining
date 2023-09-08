LOAD CSV WITH HEADERS FROM 'file:///main_new_data.csv' AS row

MERGE (startNode:Node {name: row.U})
MERGE (endNode:Node {name: row.V})
SET startNode.pi = row.u_pi
SET endNode.pi = row.v_pi
SET startNode.region = row.Region_u
SET endNode.region = row.Region_v

WITH row, startNode, endNode,
     CASE WHEN row.Type IS NULL THEN "UNDEFINED" ELSE row.Type END AS relType

FOREACH (relTypeValue IN CASE WHEN relType = "Type 1" THEN [1] ELSE [] END |
  MERGE (startNode)-[rel:FACULTY]->(endNode)
  SET rel.Gender = row.Gender, rel.Rank = row.Rank, rel.delta_pi = toFloat(row.v_pi) - toFloat(row.u_pi)
  MERGE (endNode)-[revRel:FACULTY]->(startNode)
  SET revRel.Gender = row.Gender, revRel.Rank = row.Rank, revRel.delta_pi = toFloat(row.v_pi) - toFloat(row.u_pi)
)

FOREACH (relTypeValue IN CASE WHEN relType = "Type 2" THEN [1] ELSE [] END |
  MERGE (startNode)<-[rel:FACULTY_3]-(endNode)
  SET rel.Gender = row.Gender, rel.Rank = row.Rank, rel.delta_pi = toFloat(row.v_pi) - toFloat(row.u_pi)
  MERGE (endNode)<-[revRel:FACULTY]-(startNode)
  SET revRel.Gender = row.Gender, revRel.Rank = row.Rank, revRel.delta_pi = toFloat(row.v_pi) - toFloat(row.u_pi)
)

FOREACH (relTypeValue IN CASE WHEN relType = "Type 3" THEN [1] ELSE [] END |
  MERGE (startNode)-[rel:FACULTY_3]->(endNode)
  SET rel.Gender = row.Gender, rel.Rank = row.Rank, rel.delta_pi = toFloat(row.v_pi) - toFloat(row.u_pi)
  MERGE (endNode)-[revRel:FACULTY]->(startNode)
  SET revRel.Gender = row.Gender, revRel.Rank = row.Rank, revRel.delta_pi = toFloat(row.v_pi) - toFloat(row.u_pi)
)

RETURN row, startNode, endNode LIMIT 50;
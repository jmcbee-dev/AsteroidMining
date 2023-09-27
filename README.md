# AsteroidMining
Report on the viability of asteroid mining. 

Data was sourced from https://www.kaggle.com/sakhawat18/asteroid-dataset

# Running Locally
On a local database, run the init.sql script while copying the data over. Typically this can be done by running the following in an SQL session

`\copy aseteroid_data from dataset.csv csv header;`

The resulting schema will look like such

```mermaid
classDiagram
Class01 <|-- AveryLongClass : Cool
<<Interface>> Class01
Class09 --> C2 : Where am I?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
class Class10 {
  <<service>>
  int id
  size()
}  
```

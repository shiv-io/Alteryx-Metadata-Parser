# Alteryx Workflow Metadata Parser
Parse metadata from Alteryx workflow files. The app parses the Alteryx workflow 
.yxmd files, which are just XMLs under the hood. Outputs a CSV with data on 
nodes in the workflow.

## Why?
I'm often working on a large ETL pipeline in Alteryx and need to ensure all Join
tools have the correct join clauses (among other things). Doing this manually is cumbersome, 
so I came up with this.

## Dependencies
Python 3.7

## Usage
Supports both .yxmd and .xml files.
```
python <examine_alteryx_workflow.py> <your_alteryx_workflow.yxmd> <your_output.csv>
```

## Contributing
Fork and submit a PR. Comments and questions welcome. 

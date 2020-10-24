# !/bin/bash

# Generate a pdf of database models
# Requisites: graphviz

python manage.py graph_models -a > models.dot
dot -Tpdf models.dot > models.pdf
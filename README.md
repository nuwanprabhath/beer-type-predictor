beer-type-predictor
==============================

Neural network based beer type predictor using rating criteria.

Setup instructions for model training and testing
------------
1. Clone the project
2. Add beer_reviews.csv to data/raw folder
3. Build the docker image
<pre>
docker build -t pytorch-notebook:latest .
</pre>
3. Run the image
<pre>
docker run  -dit --rm --name beer_type_predictor -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v ${PWD}:/home/jovyan/work -v ${PWD}/src:/home/jovyan/work/src pytorch-notebook:latest
</pre>
4. Run the notebook train_model_v3 in /notebooks

Setup instructions for the API
------------
1. Clone the API git repo to the /api folder from here: [https://github.com/nuwanprabhath/nn_api](https://github.com/nuwanprabhath/nn_api)
2. Copy /models/pytorch_classification_v1.pt to /api/models
3. Copy all files in /data/processed to /api/data/processed
4. Navigate to api folder and build the Docker file
<pre>
docker build -t nn-fastapi:latest .
</pre>
2. Run the image
<pre>
docker run -dit --rm --name nn_fastapi -p 8080:80 nn-fastapi:latest
</pre>
3. Navigate to [http://localhost:8080/](http://localhost:8080/)
4. To deploy in Heroku (assuming you have setup your application)
<pre>
git push heroku master
</pre>

Heroku deployment
------------
Access the deployed version of the API here: [https://intense-atoll-50811.herokuapp.com](https://intense-atoll-50811.herokuapp.com)


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── api
    │   ├── app            <- API endpoints
    │   ├── data           
    │   │   └── processed  <- Processed data during training process.
    │   ├── models         <- Trained and serialized models, model predictions, or model summaries.
    │   └── src            <- Source code for use in this project.
    │       ├── data       <- Scripts to download or generate data.
    │       └── models     <- Scripts to train models and then use trained models to make predictions.
    │   
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

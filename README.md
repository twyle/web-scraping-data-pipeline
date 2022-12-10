# web-scraping-data-pipeline
> A web scraper built with scrapy, PostgresDB, AWS EC2, Terraform and Kibana.

To launch the application:
1. Clone the application repo:</br>

      ```sh
      git clone https://github.com/twyle/web-scraping-data-pipeline.git

      ```
2. Create the database and scraper secrets:</br>

      ```sh
      touch services/database/.env

        POSTGRES_HOST=localhost
        POSTGRES_USER=lyle
        POSTGRES_PASSWORD=lyle
        POSTGRES_DB=scrapy_quotes

    Also update  the database connection string in settings.py:

    CONNECTION_STRING = "{drivername}://{user}:{passwd}@{host}:{port}/{db_name}".format(
        drivername="postgresql",
        user="lyle",
        passwd="lyle",
        host="0.0.0.0",
        port="5432",
        db_name="scrapy_quotes",
    )
      ```

3. Launch the database and grafana:</br>

      ```sh
      docker-compose up --build
      ```

4. Launch the scraper:</br>

      ```sh
      python3 -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
      cd quotes_scraper
      scrapy crawl quotes
      ```


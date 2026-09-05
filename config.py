class Config:
    SECRET_KEY = "eduadapt_secret"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:@localhost:3306/eduadapt"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
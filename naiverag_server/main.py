from sqlmodel import SQLModel, Field, create_engine


class AuthorBase(SQLModel):
    pass

class Author(AuthorBase, table=True):
    id: int | None = Field(default=None)


class NovelBase(SQLModel):
    pass

class Novel(NovelBase, table=True):
    id: int | None = Field(default=None)


class ChapterBase(SQLModel):
    pass

class Chapter(ChapterBase, table=True):
    id: int | None = Field(default=None)

class EpisodeBase(SQLModel):
    pass

class Episode(EpisodeBase, table=True):
    id: int | None = Field(default=None)


database_url = ""
engine = create_engine(database_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def main():
    print("Hello from naiverag-pgvectorscale!")


if __name__ == "__main__":
    main()

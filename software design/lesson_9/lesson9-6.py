import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from pprint import pprint

Base = declarative_base()
DSN = 'postgresql+psycopg2://user:1111@localhost:5432/music0'
engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

track_to_genre = sq.Table(
    'track_to_genre', Base.metadata,
    sq.Column('genre_id', sq.Integer, sq.ForeignKey('genre.id')),
    sq.Column('track_id', sq.Integer, sq.ForeignKey('track.id')),
)


class Artist(Base):
    __tablename__ = 'artist'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(50), nullable=False)

    def pay_ganorar(self):
        print('payed!')

    def __str__(self):
        return f'id - {self.id}, artist_name - {self.name}'

    def __repr__(self):
        return str(self)


class Genre(Base):
    __tablename__ = 'genre'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(50), nullable=False)
    track = relationship('Track', secondary='track_to_genre', back_populates='genre')

    def __str__(self):
        return f'genre_id - {self.id}, title - {self.title}'

    def __repr__(self):
        return str(self)


class Album(Base):
    __tablename__ = 'album'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    year = sq.Column(sq.Integer)
    tracks = relationship('Track', backref='album')
    # published = sq.Column(sq.Date)
    id_artist = sq.Column(sq.Integer, sq.ForeignKey('artist.id'))
    artist = relationship(Artist)

    def __str__(self):
        return f'{self.id}: {self.title}, {self.year}'

    def __repr__(self):
        return str(self)


class Track(Base):
    __tablename__ = 'track'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    duration = sq.Column(sq.Integer)
    genre = relationship(Genre, secondary=track_to_genre, back_populates='track', cascade="delete")
    album_id = sq.Column(sq.Integer, sq.ForeignKey('album.id'))

    def __str__(self):
        return f'{self.id}: {self.title}, {self.duration}, {self.album_id}'

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    # # создаем базу \d \d album
    # Base.metadata.create_all(engine)


    # # создадим artist, album, genre, track
    # artist_ls = [Artist(name='Abba'), Artist(name='Cure'), Artist(name='Clash')]
    # session.add_all(artist_ls)
    #
    # album_ls = [Album(title='Abba', year=1970, id_artist=1),
    #             Album(title='The Top', year=1983, id_artist=2),
    #             Album(title='London calling', year=1979, id_artist=3),]
    # session.add_all(album_ls)


    rock = Genre(title='Rock')
    pop = Genre(title='pop')
    punk = Genre(title='Punk')

    session.add_all([rock, pop, punk])



    # track_ls1 = [
    #     Track(title='track1', duration=300, album_id=1),
    #     Track(title='track2', duration=350, album_id=1),
    #     Track(title='track3', duration=330, album_id=1),
    # ]
    #
    # for tr in track_ls1:
    #     tr.genre.append(pop)
    # session.add_all(track_ls1)

    # track_ls2 = [Track(title='track1', duration=300, album_id=2),
    #              Track(title='track2', duration=350, album_id=2),
    #              Track(title='track3', duration=330, album_id=2)]
    # for tr in track_ls2:
    #     tr.genre = [pop, rock]
    # session.add_all(track_ls2)


    # track_ls3 = [Track(title='track1', duration=380, album_id=3),
    #              Track(title='track2', duration=350, album_id=3),
    #              Track(title='track3', duration=290, album_id=3)]
    # for tr in track_ls3:
    #     tr.genre = [punk, rock]
    # session.add_all(track_ls3)

    felichita = Track(title='felichita', duration=500)
    session.add(felichita)
    felichita.genre = [punk, rock, pop]
    session.commit()



    print('OK')


# q = session.query(Track)
# q.filter(Track.title=='track1').all()
# q.filter(Track.title.like('track%')).all()
# q = session.query(Track).filter(Track.title.like('track%'))
# print(q)
# q = session.query(Track).join(Album).filter(Album.id == 2)
# q.all()
# track = q.all()
# track[0]
# track[0].album
# track[0].album.artist.name
# track[0].album.artist.pay_ganorar()
# session.query(Album).filter(Album.id_artist == 1).update({'year': 2023})
# session.query(Album).filter(Album.id == 1).update({'year': 2023})

# UPDATE
#     session.query(Album).filter(Album.id == 1).update({'year': "2000"})
#     session.commit()
# DELETE
#     session.query(Track).filter(Track.id == 9).delete()
#     session.commit()

    # g1 = Genre(title='Metal')
    # session.add(g1)
    # print(g1)

    # query_track = session.query(Track).join(Album).filter(Album.id == 3)
    # for track in query_track.all():
    #     track.genre.append(genre=1)
    # session.commit()





    # genre_ls = [Genre(title='Pop'), Genre(title='Rock'), Genre(title='Punk')]
    # session.add_all(genre_ls)

    # for track in track_ls3:
    #     track.genre.append(punk)
    # session.add_all(track_ls3)

    # rock = session.query(Genre).filter_by(title="Rock").first()
    # pop = session.query(Genre).filter_by(title="Pop").first()
    # punk = session.query(Genre).filter_by(title="Punk").first()
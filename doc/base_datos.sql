CREATE TABLE Movie (
  code varchar(10) PRIMARY KEY,
  name varchar(100) NOT NULL,
  image_url varchar(255),
  year int(4)
);

CREATE TABLE Review (
  id int(8) AUTO_INCREMENT PRIMARY KEY,
  name varchar(100) NOT NULL,
  email varchar(100) NOT NULL,
  description varchar(4000) NOT NULL,
  rating int(1) NOT NULL,
  code varchar(10) NOT NULL,
  CONSTRAINT review_movie_fk FOREIGN KEY (code) REFERENCES Movie (code)
);
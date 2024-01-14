import sqlite3
from edit_db import today, increase
from datetime import datetime, timedelta

conn = sqlite3.connect("tennis_club_db.db")
cur = conn.cursor()


def upload_data():
        conn.execute('''INSERT INTO athlete
                        VALUES  ('A00001', 'advanced intermediate', 'P001', '2023-01-05', '2023-01-06', '2023-01-07'),
                                ('A00002', 'professional', 'P002', '2023-04-22', '2023-04-23', '2023-05-23'),
                                ('A00003', 'junior', 'P003', '2023-09-15', '2023-09-16', '2024-09-17'),
                                ('A00004', 'professional', 'P002', '2023-03-24', '2023-03-25', '2023-04-25'),
                                ('A00005', 'junior', 'P003', '2023-08-08', '2023-08-09', '2024-08-10'),
                                ('A00006', 'intermediate', 'P002', '2023-05-15', '2023-05-16', '2023-06-16'),
                                ('A00007', 'advanced intermediate', 'P002', '2023-01-25', '2023-01-26', '2023-02-26'),
                                ('A00008', 'junior', 'P003', '2023-08-24', '2023-08-25', '2024-08-25'),
                                ('A00009', 'advanced', 'P001', '2023-03-19', '2023-03-20', '2023-03-21'),
                                ('A00010', 'advanced intermediate', 'P001', '2023-06-09', '2023-06-10', '2023-06-11'),
                                ('A00011', 'advanced intermediate', 'P002', '2024-01-07', '2024-01-07', '2024-02-07'),
                                ('A00012', 'professional', 'P003', '2023-06-24', '2023-06-25', '2024-06-25'),
                                ('A00013', 'professional', 'P002', '2024-01-10', '2024-01-10', '2024-02-10'),
                                ('A00014', 'professional', 'P003', '2023-06-22', '2023-06-23', '2024-06-23'),
                                ('A00015', 'advanced', 'P003', '2023-02-16', '2023-02-17', '2024-02-17'),
                                ('A00016', 'advanced intermediate', 'P001', '2023-08-02', '2023-08-03', '2023-08-04'),
                                ('A00017', 'advanced intermediate', 'P002', '2023-01-14', '2023-01-15', '2023-02-15'),
                                ('A00018', 'professional', 'P002', '2023-06-08', '2023-06-09', '2023-07-09'),
                                ('A00019', 'intermediate', 'P001', '2023-12-13', '2023-12-14', '2023-12-15'),
                                ('A00020', 'junior', 'P002', '2023-12-23', '2024-01-05', '2024-02-05'),
                                ('A00021', 'advanced intermediate', 'P002', '2023-09-01', '2023-09-02', '2023-10-02'),
                                ('A00022', 'professional', 'P003', '2023-08-06', '2023-08-07', '2024-08-07'),
                                ('A00023', 'junior', 'P003', '2023-12-13', '2023-12-14', '2024-12-15'),
                                ('A00024', 'intermediate', 'P002', '2023-02-01', '2023-02-02', '2023-03-02'),
                                ('A00025', 'intermediate', 'P002', '2023-09-07', '2023-09-08', '2023-10-08'),
                                ('A00026', 'junior',  'P002', '2024-01-05', '2024-01-06', '2024-01-06'),
                                ('A00027', 'intermediate', 'P002', '2023-10-01', '2023-10-02', '2023-11-02'),
                                ('A00028', 'advanced intermediate', 'P002', '2023-06-19', '2023-06-20', '2023-07-20'),
                                ('A00029', 'advanced', 'P001', '2023-01-04', '2023-01-05', '2023-01-06'),
                                ('A00030', 'advanced', 'P003', '2023-01-01', '2023-01-02', '2024-01-02'),
                                ('A00031', 'advanced', 'P003', '2023-06-24', '2023-06-25', '2024-06-25'),
                                ('A00032', 'intermediate', 'P001', '2023-05-31', '2023-06-01', '2023-06-02'),
                                ('A00033', 'intermediate', 'P001', '2023-09-22', '2023-09-23', '2023-09-24'),
                                ('A00034', 'intermediate', 'P003', '2023-10-07', '2023-10-08', '2024-10-08'),
                                ('A00035', 'beginner', 'P002', '2023-03-27', '2023-03-28', '2023-04-28'),
                                ('A00036', 'professional', 'P003', '2023-10-14', '2023-10-15', '2024-10-15'),
                                ('A00037', 'junior', 'P003', '2023-09-27', '2023-09-28', '2024-09-28'),
                                ('A00038', 'advanced intermediate', 'P001', '2023-10-06', '2023-10-07', '2023-10-08'),
                                ('A00039', 'advanced', 'P001', '2023-07-28', '2023-07-29', '2023-07-30'),
                                ('A00040', 'advanced', 'P001', '2024-01-10', '2024-01-11', '2024-01-11'),
                                ('A00041', 'intermediate', 'P001', '2023-12-29', '2023-12-30', '2023-12-31'),
                                ('A00042', 'beginner', 'P001', '2023-10-15', '2023-10-16', '2023-10-17'),
                                ('A00043', 'advanced intermediate', 'P002', '2023-12-19', '2023-12-20', '2024-01-20'),
                                ('A00044', 'beginner', 'P003', '2023-10-09', '2023-10-10', '2024-10-11'),
                                ('A00045', 'advanced', 'P001', '2023-04-12', '2023-04-13', '2023-04-14'),
                                ('A00046', 'advanced', 'P003', '2023-09-16', '2023-09-17', '2024-09-17'),
                                ('A00047', 'advanced', 'P002', '2024-01-08', '2024-01-08', '2024-02-08'),
                                ('A00048', 'junior', 'P003', '2023-09-15', '2023-09-16', '2024-09-16'),
                                ('A00049', 'advanced intermediate', 'P003', '2023-11-17', '2023-11-18', '2024-11-18'),
                                ('A00050', 'intermediate', 'P002', '2023-11-14', '2023-11-15', '2023-12-15'),
                                ('A00051', 'advanced', 'P003', '2023-11-28', '2023-11-29', '2024-11-29'),
                                ('A00052', 'advanced', 'P001', '2023-07-11', '2023-07-12', '2023-07-13'),
                                ('A00053', 'professional', 'P003', '2023-03-11', '2023-03-12', '2024-03-12'),
                                ('A00054', 'advanced intermediate', 'P001', '2023-02-23', '2023-02-24', '2023-02-25'),
                                ('A00055', 'intermediate', 'P003', '2023-03-01', '2023-03-02', '2024-03-02'),
                                ('A00056', 'intermediate', 'P001', '2023-06-10', '2023-06-11', '2023-06-12'),
                                ('A00057', 'advanced', 'P003', '2023-05-09', '2023-05-10', '2024-05-10'),
                                ('A00058', 'intermediate', 'P003', '2023-08-09', '2023-08-10', '2024-08-10'),
                                ('A00059', 'intermediate', 'P002', '2023-06-10', '2023-06-11', '2023-07-11'),
                                ('A00060', 'advanced intermediate', 'P002', '2023-08-29', '2023-08-30', '2023-09-30'),
                                ('A00061', 'beginner', 'P001', '2023-10-16', '2023-10-17', '2023-10-18'),
                                ('A00062', 'advanced intermediate', 'P002', '2023-01-06', '2023-01-07', '2023-02-07'),
                                ('A00063', 'professional', 'P001', '2023-12-25', '2023-12-26', '2023-12-27'),
                                ('A00064', 'special needs', 'P003', '2023-10-25', '2023-10-25', '2024-10-25'),
                                ('A00065', 'intermediate', 'P002', '2023-11-07', '2023-11-08', '2023-12-08'),
                                ('A00066', 'beginner', 'P002', '2024-01-04', '2024-01-05', '2024-02-05'),
                                ('A00067', 'advanced intermediate', 'P001', '2023-11-26', '2023-11-27', '2023-11-28'),
                                ('A00068', 'beginner', 'P002', '2024-01-12', '2024-01-12', '2024-02-12'),
                                ('A00069', 'advanced', 'P003', '2023-08-14', '2023-08-15', '2024-08-15'),
                                ('A00070', 'advanced intermediate', 'P001', '2023-11-20', '2023-11-21', '2023-11-22'),
                                ('A00071', 'advanced intermediate', 'P001', '2023-12-17', '2023-12-18', '2023-12-19'),
                                ('A00072', 'beginner', 'P002', '2023-03-15', '2023-03-16', '2023-04-16'),
                                ('A00073', 'intermediate', 'P001', '2023-07-07', '2023-07-08', '2023-07-09'),
                                ('A00074', 'beginner', 'P002', '2023-12-08', '2023-12-09', '2024-01-09'),
                                ('A00075', 'advanced intermediate', 'P001', '2023-04-05', '2023-04-06', '2023-04-07'),
                                ('A00076', 'professional', 'P002', '2023-04-22', '2023-04-23', '2023-05-23'),
                                ('A00077', 'intermediate', 'P002', '2023-07-29', '2023-07-30', '2023-08-30'),
                                ('A00078', 'professional', 'P001', '2023-05-31', '2023-06-01', '2023-06-02'),
                                ('A00079', 'intermediate', 'P002', '2023-09-15', '2023-09-16', '2023-10-16'),
                                ('A00080', 'advanced intermediate', 'P001', '2023-09-16', '2023-09-17', '2023-09-18'),
                                ('A00081', 'beginner', 'P003', '2023-11-04', '2023-11-05', '2024-11-05'),
                                ('A00082', 'special needs', 'P002', '2024-01-07', '2024-01-17', '2024-02-17'),
                                ('A00083', 'special needs', 'P003', '2023-12-01', '2023-12-01', '2024-12-01'),
                                ('A00084', 'beginner', 'P003', '2023-08-18', '2023-08-19', '2024-08-19'),
                                ('A00085', 'intermediate', 'P002', '2023-12-29', '2023-12-30', '2024-01-30'),
                                ('A00086', 'intermediate', 'P003', '2023-09-03', '2023-09-04', '2024-09-04'),
                                ('A00087', 'beginner', 'P002', '2024-01-05', '2024-01-06', '2024-02-05'),
                                ('A00088', 'special needs', 'P003', '2023-12-20', '2023-12-21', '2024-12-20'),
                                ('A00089', 'advanced', 'P002', '2023-12-18', '2023-12-19', '2024-01-19'),
                                ('A00090', 'professional', 'P003', '2023-08-03', '2023-08-04', '2024-08-04'),
                                ('A00091', 'intermediate', 'P002', '2023-05-07', '2023-05-08', '2023-06-08'),
                                ('A00092', 'beginner', 'P003', '2023-07-25', '2023-07-26', '2024-07-26'),
                                ('A00093', 'advanced intermediate', 'P003', '2023-01-18', '2023-01-19', '2024-01-19'),
                                ('A00094', 'professional', 'P002', '2023-09-13', '2023-09-14', '2023-10-14'),
                                ('A00095', 'special needs', 'P002', '2024-01-05', '2024-01-05', '2024-02-05'),
                                ('A00096', 'intermediate', 'P001', '2023-11-13', '2023-11-14', '2023-11-15'),
                                ('A00097', 'advanced', 'P002', '2023-12-30', '2023-12-31', '2024-01-31'),
                                ('A00098', 'intermediate', 'P002', '2023-03-04', '2023-03-05', '2023-04-05'),
                                ('A00099', 'advanced intermediate', 'P002', '2024-01-08', '2024-01-08', '2024-02-07'),
                                ('A00100', 'advanced', 'P002', '2024-01-11', '2024-01-11', '2024-02-11');
                                ''')

        conn.execute('''INSERT INTO coach
                VALUES  ('C00001', 'junior'),
                        ('C00002', 'junior'),
                        ('C00003', 'beginners'),
                        ('C00004', 'beginners'),
                        ('C00005', 'advanced'),
                        ('C00006', 'advanced'),
                        ('C00007', 'advanced'),
                        ('C00008', 'high-performance'),
                        ('C00009', 'high-performance'),
                        ('C00010', 'special needs');
                        ''')

        conn.execute('''INSERT INTO member
                VALUES  ('Nikos', 'Papadopoulos', '2017-11-18', '5351693091', 'nikos.papadopoulos.1985@gmail.com', '1973-11-19', '45 Odos Ermou, Patras', 'A00001'),
                        ('Eleni', 'Karagianni', '2017-05-16', '9523410732', 'eleni.karagianni.93@gmail.com', '2007-01-11', '78 Leoforos Kifisias, Patras', 'A00002'),
                        ('Dimitris', 'Georgiou', '2015-05-28', '5594470441', 'dimitris.georgiou.76@gmail.com', '1970-07-04', '22 Ethnikis Antistaseos, Patras', 'A00003'),
                        ('Maria', 'Ioannou', '2013-03-01', '7774798831', 'maria.ioannou.84@gmail.com', '1996-04-28', '37 Leoforos Eleftheriou Venizelou, Patras', 'A00004'),
                        ('Giorgos', 'Papadakis', '2014-06-19', '8851403635', 'giorgos.papadakis.77@gmail.com', '2007-06-13', '101 Vasileos Georgiou, Patras', 'A00005'),
                        ('Katerina', 'Katsarou', '2018-09-02', '1772119929', 'katerina.katsarou.89@gmail.com', '2009-01-03', '101 Ethnikis Antistaseos, Rio', 'A00006'),
                        ('Andreas', 'Antoniou', '2016-01-04', '2688557763', 'andreas.antoniou.82@gmail.com', '2005-08-28', '80 Kapodistriou, Rio', 'A00007'),
                        ('Sophia', 'Vlachou', '2020-06-26', '6474698096', 'sophia.vlachou@gmail.com', '1991-10-18', '19 Dimosthenous, Rio', 'A00008'),
                        ('Panagiotis', 'Kouros', '2013-02-19', '9454388597', 'panagiotis.kouros.87@gmail.com', '1983-05-16', '92 Agiou Nikolaou, Rio', 'A00009'),
                        ('Ioanna', 'Andreadi', '2010-04-06', '8343506592', 'ioanna.andreadi.1990@gmail.com', '2006-08-04', '48 Plateia Eleftherias, Rio', 'A00010'),
                        ('Thanos', 'Kostopoulos', '2021-01-10', '7226156921', 'thanos.kostopoulos.80@gmail.com', '1987-06-26', '91 Elpidos, Aigio', 'A00011'),
                        ('Despina', 'Kolouri', '2011-04-09', '5244838103', 'despina.kolouri.88@gmail.com', '1981-06-08', '20 Plateia Kritis, Aigio', 'A00012'),
                        ('Kostas', 'Mastrogiannis', '2010-08-27', '9375939398', 'kostas.mastrogiannis.91@gmail.com', '1987-06-10', '71 Tsimiski, Aigio', 'A00013'),
                        ('Anna', 'Papadopoulou', '2015-12-19', '6075804449', 'anna.papadopoulou.94@gmail.com', '1993-06-13', '45 Kountouriotou, Aigio', 'A00014'),
                        ('Katerina', 'Tsarantani', '2011-02-22', '7266297419', 'christos.nikolaidis.75@gmail.com', '1993-03-17', '37 Ethnikis Antistaseos, Aigio', 'A00015'),
                        ('Eleni', 'Tsoukala', '2021-10-09', '3359574005', 'eleni.tsoukala.1983@gmail.com', '1983-12-27', '67 Kifissou, Kato Achaia', 'A00016'),
                        ('Petros', 'Vassilopoulos', '2010-10-15', '6619628559', 'petros.vassilopoulos.79@gmail.com', '1981-10-30', '88 Leoforos Vasileos Pavlou, Kato Achaia', 'A00017'),
                        ('Alexandra', 'Papageorgiou', '2018-11-28', '6391611064', 'alexandra.papageorgiou@gmail.com', '1981-12-11', '71 Ermou, Kato Achaia', 'A00018'),
                        ('Spiros', 'Papadimitriou', '2010-12-28', '9088429411', 'spiros.papadimitriou.86@gmail.com', '1988-04-27', '77 Agiou Konstantinou, Athens', 'A00019'),
                        ('Christina', 'Christodoulou', '2021-04-26', '8318403329', 'christina.christodoulou.92@gmail.com', '1997-12-18', '28 Odos Agamemnonos, Athens', 'A00020'),
                        ('Stavros', 'Alexopoulos', '2016-11-28', '2879354528', 'stavros.alexopoulos.78@gmail.com', '1980-05-28', '32 Irakliou, Psathopyrgos', 'A00021'),
                        ('Vasiliki', 'Nikolaidi', '2015-01-16', '4079651475', 'vasiliki.nikolaidi.85@gmail.com', '1987-03-19', '15 Plateia Omonias, Psathopyrgos', 'A00022'),
                        ('Tasos', 'Tsoukalas', '2012-01-12', '5523989604', 'tasos.tsoukalas.89@gmail.com', '1983-03-18', '67 Michail Karaoli, Psathopyrgos', 'A00023'),
                        ('Theodora', 'Sotiriou', '2021-05-04', '6487181613', 'theodora.sotiriou.90@gmail.com', '2004-04-10', '64 Dimokratias, Psathopyrgos', 'A00024'),
                        ('Michalis', 'Papazoglou', '2019-08-12', '7718554348', 'michalis.papazoglou@gmail.com', '1983-03-04', '17 Kifissou, Psathopyrgos', 'A00025'),
                        ('Angeliki', 'Panagiotopoulou', '2011-04-28', '9678272876', 'angeliki.panagiotopoulou.1984@gmail.com', '1990-07-16', '41 Emmanouil Benaki, Nafpaktos', 'A00026'),
                        ('Apostolis', 'Antoniou', '2021-06-15', '6038075624', 'apostolis.antoniou.81@gmail.com', '1974-05-01', '50 Plateia Venizelou, Nafpaktos', 'A00027'),
                        ('Athina', 'Georgiou', '2022-06-10', '9746099376', 'athina.georgiou.76@gmail.com', '2008-01-26', '41 Leoforos Agiou Nikolaou, Nafpaktos', 'A00028'),
                        ('Yannis', 'Perdikis', '2017-03-14', '9987317691', 'yannis.perdikis@gmail.com', '2000-10-09', '54 Eleftheriou Venizelou, Nafpaktos', 'A00029'),
                        ('Irini', 'Karali', '2014-07-08', '6657062742', 'irini.karali.88@gmail.com', '1997-01-03', '65 Elpidos, Nafpaktos', 'A00030'),
                        ('Vangelis', 'Efthimiou', '2013-05-25', '2277296545', 'vangelis.efthimiou.82@gmail.com', '1999-10-22', '29 Politechniou, Patras', 'A00031'),
                        ('Anna', 'Papadimitriou', '2013-01-12', '7619407416', 'anna.papadimitriou.77@gmail.com', '2004-01-29', '14 Akadimias, Patras', 'A00032'),
                        ('Dimitra', 'Eleftheriou', '2021-08-30', '1412533755', 'dimitra.eleftheriou@gmail.com', '1986-05-13', '72 Mesologgiou, Patras', 'A00033'),
                        ('Manolis', 'Filippopoulos', '2011-10-29', '6392278544', 'manolis.filippopoulos.80@gmail.com', '1994-01-21', '22 Aristotelous, Patras', 'A00034'),
                        ('Margarita', 'Marini', '2015-05-16', '4916345981', 'margarita.marini@gmail.com', '1997-02-04', '5 Papanikolaou, Patras', 'A00035'),
                        ('Antonis', 'Tzortzis', '2022-02-11', '8929116739', 'antonis.tzortzis.74@gmail.com', '2003-04-19', '81 Leoforos Eleftheriou Venizelou, Rio', 'A00036'),
                        ('Zoe', 'Samara', '2017-11-29', '2899889089', 'zoe.samara.85@gmail.com', '2007-11-20', '79 Eleftheriou Venizelou, Rio', 'A00037'),
                        ('Constantinos', 'Kourakis', '2012-06-21', '4696071498', 'constantinos.kourakis.89@gmail.com', '2003-01-01', '27 Vilara, Rio', 'A00038'),
                        ('Eirini', 'Vassilopoulou', '2011-12-29', '3897474594', 'eirini.vassilopoulou@gmail.com', '1999-09-17', '14 Agiou Ioannou, Rio', 'A00039'),
                        ('Alexandros', 'Tsakalidis', '2019-11-03', '5037722097', 'alexandros.tsakalidis.84@gmail.com', '2015-01-07', '20 Plateia Kritis, Rio', 'A00040'),
                        ('Alexandra', 'Ioannou', '2015-07-28', '4168603371', 'alexandra.ioannou@gmail.com', '1975-11-19', '14 Agiou Nikolaou, Aigio', 'A00041'),
                        ('Anastasia', 'Karydi', '2019-09-21', '1801218979', 'anastasia.karydi.79@gmail.com', '1998-09-01', '99 Kapodistriou, Aigio', 'A00042'),
                        ('Katerina', 'Papakonstantinou', '2017-10-11', '2603695160', 'katerina.papakonstantinou.83@gmail.com', '1984-01-20', '41 Leoforos Agiou Nikolaou, Aigio', 'A00043'),
                        ('Dimitris', 'Kanellopoulos', '2019-06-29', '8978422840', 'dimitris.kanellopoulos.92@gmail.com', '1994-02-22', '36 Agias Sofias, Aigio', 'A00044'),
                        ('Angeliki', 'Papoutsi', '2021-07-04', '8234691592', 'angeliki.papoutsi.81@gmail.com', '1975-07-28', '71 Tsimiski, Aigio', 'A00045'),
                        ('Ioannis', 'Tsiamis', '2014-06-19', '2505178330', 'ioannis.tsiamis@gmail.com', '1981-09-14', '11 Kountouriotou, Kato Achaia', 'A00046'),
                        ('Daphne', 'Antoniou', '2015-12-23', '8033866576', 'daphne.antoniou@gmail.com', '1995-08-15', '32 Irakliou, Kato Achaia', 'A00047'),
                        ('Constantinos', 'Kalogerakis', '2022-03-04', '9568885463', 'constantinos.kalogerakis.77@gmail.com', '1975-01-13', '101 Ethnikis Antistaseos, Kato Achaia', 'A00048'),
                        ('Kalliopi', 'Samara', '2019-11-03', '1788000114', 'kalliopi.samara@gmail.com', '2007-04-10', '91 Elpidos, Kato Achaia', 'A00049'),
                        ('Theodoros', 'Kalogerakis', '2019-06-01', '6847955190', 'theodoros.kalogerakis.86@gmail.com', '1993-03-23', '11 Leoforos Thiseos, Kato Achaia', 'A00050'),
                        ('Niki', 'Perdiki', '2010-07-23', '2687457962', 'niki.perdiki.87@gmail.com', '1992-07-26', '54 Eleftheriou Venizelou, Psathopyrgos', 'A00051'),
                        ('Olga', 'Karydi', '2017-12-23', '9725551996', 'olga.karydi.90@gmail.com', '2004-06-22', '67 Michail Karaoli, Psathopyrgos', 'A00052'),
                        ('Nikitas', 'Eleftheriou', '2013-08-26', '9635951548', 'nikitas.eleftheriou@gmail.com', '1995-10-07', '66 Ethnikis Antistaseos, Psathopyrgos', 'A00053'),
                        ('Evaggelos', 'Karatzas', '2022-03-04', '6502268084', 'evaggelos.karatzas@gmail.com', '2013-11-26', '22 Ploutarchou, Psathopyrgos', 'A00054'),
                        ('Eleni', 'Louka', '2021-03-11', '9589566879', 'eleni.louka@gmail.com', '2011-01-29', '81 Leoforos Eleftheriou Venizelou, Psathopyrgos', 'A00055'),
                        ('Nikolas', 'Deligiannis', '2017-08-20', '8111552016', 'nikolas.deligiannis.84@gmail.com', '1985-01-16', '15 Plateia Omonias, Nafpaktos', 'A00056'),
                        ('Marina', 'Papoutsi', '2014-11-12', '4692402420', 'marina.papoutsi.85@gmail.com', '2010-09-26', '80 Kapodistriou, Nafpaktos', 'A00057'),
                        ('Stelios', 'Katsaros', '2011-11-03', '4058161142', 'stelios.katsaros@gmail.com', '1971-12-28', '14 Akadimias, Nafpaktos', 'A00058'),
                        ('Chrysa', 'Papathanasiou', '2021-12-07', '5381736964', 'chrysa.papathanasiou.88@gmail.com', '2009-12-15', '28 Odos Agamemnonos, Nafpaktos', 'A00059'),
                        ('Pavlos', 'Petrakis', '2019-03-10', '3947891891', 'pavlos.petrakis.82@gmail.com', '2000-07-20', '19 Dimosthenous, Nafpaktos', 'A00060'),
                        ('Rania', 'Papadopoulou', '2020-10-20', '9056740041', 'rania.papadopoulou.86@gmail.com', '2008-07-23', '63 Vilara, Patras', 'A00061'),
                        ('Georgios', 'Vrettos', '2022-03-21', '6561259947', 'georgios.vrettos@gmail.com', '1986-04-18', '41 Leoforos Agiou Nikolaou, Patras', 'A00062'),
                        ('Vicky', 'Karakosta', '2011-02-13', '9159229766', 'vicky.karakosta.89@gmail.com', '1987-09-26', '50 Plateia Venizelou, Patras', 'A00063'),
                        ('Ioannis', 'Theou', '2018-09-19', '3363716694', 'ioannis.theou.93@gmail.com', '2005-05-04', '92 Agiou Ioannou, Patras', 'A00064'),
                        ('Maria', 'Psarrou', '2014-03-18', '1559103870', 'maria.psarrou@gmail.com', '1989-09-20', '37 Leoforos Eleftheriou Venizelou, Patras', 'A00065'),
                        ('Alexandros', 'Ioannou', '2017-09-29', '4951183867', 'alexandros.ioannou.84@gmail.com', '1991-08-09', '66 Ethnikis Antistaseos, Rio', 'A00066'),
                        ('Nikos', 'Chrysovergis', '2023-01-24', '2524527022', 'nikos.chrysovergis@gmail.com', '1979-09-11', '29 Politechniou, Rio', 'A00067'),
                        ('Athina', 'Karypidi', '2011-07-21', '1452894812', 'athina.karypidi@gmail.com', '1998-11-02', '5 Elpidos, Rio', 'A00068'),
                        ('Artemis', 'Papavasileiou', '2018-02-07', '3439991267', 'artemis.papavasileiou@gmail.com', '2013-10-27', '17 Kifissou, Rio', 'A00069'),
                        ('Apostolos', 'Hatzis', '2011-01-30', '4261561816', 'apostolos.hatzis.77@gmail.com', '1978-04-03', '17 Megalou Alexandrou, Rio', 'A00070'),
                        ('Marios', 'Koliopoulos', '2023-05-27', '2193655947', 'marios.koliopoulos@gmail.com', '2002-10-09', '81 Plateia Eleftheriou Venizelou, Aigio', 'A00071'),
                        ('Manos', 'Mouratidis', '2020-01-30', '4527916334', 'manos.mouratidis@gmail.com', '2011-05-02', '20 Plateia Kritis, Aigio', 'A00072'),
                        ('Eleni', 'Panagiotou', '2022-10-12', '6522710619', 'eleni.panagiotou.79@gmail.com', '2001-02-20', '14 Dimokratias, Aigio', 'A00073'),
                        ('Marios', 'Sevastos', '2016-09-18', '5407123201', 'marios.sevastos.81@gmail.com', '1971-12-09', '37 Ethnikis Antistaseos, Aigio', 'A00074'),
                        ('Melina', 'Xanthopoulou', '2020-08-11', '5526008980', 'melina.xanthopoulou@gmail.com', '1985-07-06', '33 Kallidromiou, Aigio', 'A00075'),
                        ('Ioannis', 'Zervos', '2010-11-27', '4415652009', 'ioannis.zervos.87@gmail.com', '1998-09-22', '29 Agias Sofias, Kato Achaia', 'A00076'),
                        ('Thanos', 'Kordalis', '2021-03-18', '5608497707', 'thanos.kordalis@gmail.com', '1977-08-11', '65 Elpidos, Kato Achaia', 'A00077'),
                        ('Dimitris', 'Patsis', '2016-02-28', '5451975613', 'dimitris.patsis.85@gmail.com', '1990-09-08', '99 Kapodistriou, Kato Achaia', 'A00078'),
                        ('Kyriaki', 'Sotiriou', '2020-08-11', '7657644140', 'kyriaki.sotiriou.86@gmail.com', '2012-08-20', '11 Kountouriotou, Kato Achaia', 'A00079'),
                        ('Michalis', 'Koukoulis', '2015-05-06', '2847841306', 'michalis.koukoulis@gmail.com', '2006-08-25', '71 Tsimiski, Kato Achaia', 'A00080'),
                        ('Eleftheria', 'Antonopoulou', '2023-01-24', '1398856668', 'eleftheria.antonopoulou@gmail.com', '2008-10-27', '15 Plateia Omonias, Psathopyrgos', 'A00081'),
                        ('Alexandros', 'Christopoulos', '2019-05-29', '2171357491', 'alexandros.christopoulos@gmail.com', '2008-11-19', '57 Grigoriou Lampraki, Psathopyrgos', 'A00082'),
                        ('Katerina', 'Nikolopoulou', '2014-06-30', '3186531101', 'katerina.nikolopoulou@gmail.com', '1981-12-16', '88 Leoforos Vasileos Pavlou, Psathopyrgos', 'A00083'),
                        ('Nikos', 'Papanikolaou', '2019-10-27', '6538441538', 'nikos.papanikolaou.82@gmail.com', '1972-10-31', '78 Leoforos Kifisias, Psathopyrgos', 'A00084'),
                        ('Maria', 'Kyriazi', '2021-06-29', '2776505320', 'maria.kyriazi.84@gmail.com', '2000-01-07', '81 Leoforos Eleftheriou Venizelou, Psathopyrgos', 'A00085'),
                        ('Aris', 'Mavridis', '2023-11-13', '1571224245', 'aris.mavridis.78@gmail.com', '2015-11-19', '32 Irakliou, Nafpaktos', 'A00086'),
                        ('Glykeria', 'Terzi', '2023-06-22', '7399509668', 'glykeria.terzi@gmail.com', '2013-10-19', '48 Plateia Eleftherias, Nafpaktos', 'A00087'),
                        ('Antonis', 'Zachariadis', '2019-10-27', '5599499657', 'antonis.zachariadis.79@gmail.com', '2015-01-24', '41 Emmanouil Benaki, Nafpaktos', 'A00088'),
                        ('Chrysa', 'Panagiotou', '2019-07-19', '9636015396', 'chrysa.panagiotou.91@gmail.com', '2000-05-30', '79 Eleftheriou Venizelou, Nafpaktos', 'A00089'),
                        ('Themis', 'Koukoulis', '2021-08-23', '9626357609', 'themis.koukoulis.83@gmail.com', '1990-01-13', '45 Odos Ermou, Nafpaktos', 'A00090'),
                        ('Katerina', 'Eleftheriou', '2013-01-01', '8917375734', 'katerina.eleftheriou.92@gmail.com', '2002-04-19', '77 Agiou Konstantinou, Patras', 'A00091'),
                        ('Andreas', 'Papadopoulos', '2021-10-30', '4648684750', 'andreas.papadopoulos.87@gmail.com', '1993-02-09', '72 Mesologgiou, Patras', 'A00092'),
                        ('Panos', 'Eleftheriou', '2023-09-29', '6326268615', 'panos.eleftheriou.89@gmail.com', '1978-02-18', '20 Plateia Kritis, Patras', 'A00093'),
                        ('Niki', 'Ralli', '2022-08-18', '6339180313', 'niki.ralli.88@gmail.com', '2008-06-19', '65 Elpidos, Patras', 'A00094'),
                        ('Anna-Maria', 'Valavani', '2022-04-03', '6165219142', 'anna-maria.valavani.93@gmail.com', '2013-09-28', '14 Akadimias, Patras', 'A00095'),
                        ('Spyros', 'Zikos', '2012-12-02', '8385911909', 'spyros.zikos.86@gmail.com', '1994-03-29', '64 Dimokratias, Rio', 'A00096'),
                        ('Elena', 'Fotiou', '2017-09-04', '3912817081', 'elena.fotiou.84@gmail.com', '1999-02-07', '27 Vilara, Rio', 'A00097'),
                        ('Christoforos', 'Rodos', '2012-11-14', '8622557628', 'christoforos.rodos.90@gmail.com', '2002-02-06', '71 Tsimiski, Rio', 'A00098'),
                        ('Eirini', 'Hatzi', '2012-03-16', '4771833483', 'eirini.hatzi@gmail.com', '1979-02-15', '11 Leoforos Thiseos, Rio', 'A00099'),
                        ('Alexandros', 'Iliopoulos', '2013-02-23', '3626645946', 'alexandros.iliopoulos.82@gmail.com', '1992-02-27', '67 Michail Karaoli, Rio', 'A00100'),
                        ('Katerina', 'Ioannidi', '2015-04-26', '3735782564', 'katerina.ioannidi@gmail.com', '1987-07-07', '37 Leoforos Eleftheriou Venizelou, Aigio', 'C00001'),
                        ('Nikitas', 'Kakogiannis', '2016-08-11', '1475181875', 'nikitas.kakogiannis@gmail.com', '1996-01-04', '80 Kapodistriou, Aigio', 'C00002'),
                        ('Marios', 'Rodopoulos', '2011-04-26', '9851655010', 'marios.rodopoulos.81@gmail.com', '1992-02-05', '14 Akadimias, Aigio', 'C00003'),
                        ('Aris', 'Kosmidis', '2011-02-22', '8579184062', 'aris.kosmidis.87@gmail.com', '1977-08-01', '19 Dimosthenous, Aigio', 'C00004'),
                        ('Foteini', 'Kourtidi', '2020-10-27', '3575268404', 'foteini.kourtidi@gmail.com', '1999-09-06', '66 Ethnikis Antistaseos, Aigio', 'C00005'),
                        ('Antonios', 'Maltezos', '2012-06-01', '6556768400', 'antonios.maltezos.79@gmail.com', '1990-10-08', '50 Plateia Venizelou, Patras', 'C00006'),
                        ('Chrysa', 'Mpoura', '2019-08-01', '6868336292', 'chrysa.mpoura.88@gmail.com', '1979-10-28', '32 Irakliou, Kato Achaia', 'C00007'),
                        ('Themis', 'Nikolaou', '2015-08-19', '1962664779', 'themis.nikolaou@gmail.com', '1992-11-21', '11 Kountouriotou, Patras', 'C00008'),
                        ('Kostas', 'Petrou', '2011-01-13', '9522797646', 'kostas.petrou.86@gmail.com', '2003-09-26', '91 Elpidos, Rio', 'C00009'),
                        ('Andreas', 'Zikos', '2017-07-27', '2838311684', 'andreas.zikos.89@gmail.com', '1995-05-16', '22 Ethnikis Antistaseos, Patras', 'C00010');
                     ''')

        conn.execute('''INSERT INTO court 
                VALUES  ('CR01', 'clay'),
                        ('CR02', 'clay'),
                        ('CR03', 'clay'),
                        ('CR04', 'grass'),
                        ('CR05', 'grass'),
                        ('CR06', 'hard'),
                        ('CR07', 'hard');
                     ''')

        conn.execute('''INSERT INTO package
                VALUES  ('P001', 'day'),
                        ('P002', 'month'),
                        ('P003', 'year');
                        ''')

        conn.execute('''INSERT INTO reservation
                VALUES  ('R00001', '2024-02-18', '19:30', 1.5, '2023-12-02', 'A00008', 'CR05', NULL),
                        ('R00002', '2024-01-10', '15:00', 2.0, '2023-12-30', 'A00041', 'CR05', NULL),
                        ('R00003', '2024-02-26', '13:30', 1.0, '2023-12-13', 'A00008', 'CR07', 'R00001'),
                        ('R00004', '2024-01-05', '14:00', 1.0, '2023-12-20', 'A00012', 'CR01', NULL),
                        ('R00005', '2024-01-17', '17:30', 1.5, '2023-12-03', 'A00014', 'CR02', NULL),
                        ('R00006', '2024-02-26', '8:00', 1.0, '2023-12-24', 'A00015', 'CR04', NULL),
                        ('R00007', '2024-01-28', '14:30', 1.5, '2023-12-02', 'A00015', 'CR05', NULL),
                        ('R00008', '2024-01-11', '19:30', 4.0, '2023-12-01', 'A00030', 'CR03', NULL),
                        ('R00009', '2024-02-22', '8:00', 1.5, '2023-12-01', 'A00048', 'CR07', NULL),
                        ('R00010', '2024-02-02', '19:00', 2.5, '2023-12-19', 'A00051', 'CR07', NULL),
                        ('R00011', '2024-01-18', '18:00', 1.0, '2023-12-12', 'A00069', 'CR03', NULL),
                        ('R00012', '2024-01-07', '7:30', 4.0, '2023-12-10', 'A00030', 'CR06', 'R00008'),
                        ('R00013', '2024-01-03', '19:00', 2.0, '2023-12-21', 'A00097', 'CR04', NULL),
                        ('R00014', '2024-01-15', '17:00', 1.0, '2023-12-26', 'A00063', 'CR03', NULL),
                        ('R00015', '2024-02-11', '9:00', 2.0, '2023-12-04', 'A00034', 'CR02', NULL),
                        ('R00016', '2024-02-20', '21:00', 4.0, '2023-12-03', 'A00043', 'CR02', NULL),
                        ('R00017', '2024-02-19', '21:00', 3.0, '2023-12-22', 'A00083', 'CR05', NULL),
                        ('R00018', '2024-01-24', '16:30', 3.0, '2023-12-12', 'A00046', 'CR06', NULL),
                        ('R00019', '2024-02-03', '13:30', 1.5, '2023-12-24', 'A00074', 'CR05', NULL),
                        ('R00020', '2024-02-28', '20:30', 2.0, '2023-12-11', 'A00051', 'CR07', NULL),
                        ('R00021', '2024-02-25', '10:00', 1.5, '2023-12-02', 'A00084', 'CR05', NULL),
                        ('R00022', '2024-01-14', '9:30', 2.5, '2023-12-11', 'A00058', 'CR05', NULL),
                        ('R00023', '2024-01-31', '8:30', 1.5, '2023-12-18', 'A00046', 'CR02', NULL),
                        ('R00024', '2024-02-12', '16:00', 3.5, '2023-12-15', 'A00069', 'CR04', NULL),
                        ('R00025', '2024-01-02', '8:00', 1.5, '2023-12-30', 'A00074', 'CR01', NULL),
                        ('R00026', '2024-01-16', '18:30', 3.5, '2023-12-06', 'A00074', 'CR05', NULL),
                        ('R00027', '2024-01-20', '10:00', 2.0, '2023-12-23', 'A00036', 'CR01', NULL),
                        ('R00028', '2024-01-09', '9:30', 2.5, '2023-12-20', 'A00097', 'CR06', NULL),
                        ('R00029', '2024-02-01', '9:30', 1.5, '2023-12-05', 'A00093', 'CR05', NULL),
                        ('R00030', '2024-01-23', '8:00', 2.0, '2023-12-07', 'A00081', 'CR03', NULL),
                        ('R00031', '2024-01-25', '9:00', 3.5, '2023-12-17', 'A00084', 'CR03', NULL),
                        ('R00032', '2024-01-18', '17:00', 3.0, '2023-12-18', 'A00085', 'CR04', NULL),
                        ('R00033', '2024-02-08', '20:00', 1.0, '2023-12-21', 'A00092', 'CR02', NULL),
                        ('R00034', '2024-02-22', '19:30', 3.5, '2023-12-26', 'A00053', 'CR05', NULL),
                        ('R00035', '2024-01-29', '8:00', 2.0, '2023-12-11', 'A00093', 'CR04', NULL),
                        ('R00036', '2024-02-05', '20:00', 3.5, '2023-12-22', 'A00014', 'CR03', NULL),
                        ('R00037', '2024-02-16', '19:30', 2.0, '2023-12-28', 'A00008', 'CR02', 'R00003'),
                        ('R00038', '2024-01-28', '9:30', 3.0, '2023-12-08', 'A00097', 'CR02', NULL),
                        ('R00039', '2024-02-18', '19:30', 1.0, '2023-12-23', 'A00051', 'CR03', NULL),
                        ('R00040', '2024-02-27', '20:30', 3.0, '2023-12-20', 'A00030', 'CR07', NULL),
                        ('R00041', '2024-01-01', '15:00', 1.0, '2023-12-10', 'C00001', 'CR05', NULL),
                        ('R00042', '2024-01-26', '15:00', 4.0, '2023-12-12', 'C00002', 'CR04', NULL),
                        ('R00043', '2024-01-11', '15:00', 1.5, '2023-12-26', 'C00003', 'CR07', NULL),
                        ('R00044', '2024-02-22', '8:30', 3.5, '2023-12-29', 'C00004', 'CR01', NULL),
                        ('R00045', '2024-01-08', '18:30', 1.5, '2023-12-17', 'C00005', 'CR01', NULL),
                        ('R00046', '2024-02-06', '9:30', 2.0, '2023-12-15', 'C00006', 'CR01', NULL),
                        ('R00047', '2024-01-29', '11:30', 1.0, '2023-12-30', 'C00007', 'CR04', NULL),
                        ('R00048', '2024-01-26', '10:00', 1.0, '2023-12-08', 'C00008', 'CR05', NULL),
                        ('R00049', '2024-02-21', '15:30', 2.0, '2023-12-31', 'C00009', 'CR06', NULL);
                        ''')

        conn.execute('''INSERT INTO equipment
                VALUES  ('E001', 'standard balls', 1, '2023-06-01', 'A00032'),
                        ('E002', 'accessories', 3, '2023-01-24', 'A00017'),
                        ('E003', 'racquet', 1, '2023-01-06', 'A00001'),
                        ('E004', 'accessories', 1, '2023-08-02', 'A00011'),
                        ('E005', 'racquet', 2, '2023-02-08', 'A00020'),
                        ('E006', 'apparel', 3, '2023-08-19', 'A00084'),
                        ('E007', 'standard balls', 3, '2023-11-29', 'A00051'),
                        ('E008', 'shoes', 1, '2023-02-23', 'A00024'),
                        ('E009', 'standard balls', 1, '2023-08-19', 'A00084'),
                        ('E010', 'pressureless balls', 2, '2023-12-19', 'A00071'),
                        ('E011', 'apparel', 2, '2023-09-03', 'A00095'),
                        ('E012', 'pressureless balls', 3, '2023-02-25', 'A00054'),
                        ('E013', 'shoes', 2, '2023-09-17', 'A00046'),
                        ('E014', 'bag', 1, '2023-06-10', 'A00006'),
                        ('E015', 'pressureless balls', 2, '2023-09-11', 'A00089'),
                        ('E016', 'shoes', 2, '2023-01-02', 'A00085'),
                        ('E017', 'pressureless balls', 3, '2023-10-17', 'A00042'),
                        ('E018', 'bag', 2, '2023-10-18', 'A00061'),
                        ('E019', 'standard balls', 2, '2023-09-19', 'A00060'),
                        ('E020', 'bag', 1, '2023-12-11', 'A00081'),
                        ('E021', 'shoes', 1, '2023-01-06', 'A00029'),
                        ('E022', 'racquet', 3, '2023-12-20', 'A00074'),
                        ('E023', 'standard balls', 3, '2023-11-22', 'A00070'),
                        ('E024', 'shoes', 3, '2023-11-30', 'A00065'),
                        ('E025', 'bag', 3, '2023-08-08', 'A00022');     
                        ''')




        conn.execute('''INSERT INTO match
                VALUES  ('M001', 2, '2023-12-05', '10:00', 2, 'CR05'),
                        ('M002', 2, '2023-12-20', '16:30', 2, 'CR01'),
                        ('M003', 2, '2023-12-15', '10:00', 2, 'CR04'),
                        ('M004', 4, '2023-12-22', '12:00', 2, 'CR03'),
                        ('M005', 2, '2024-01-06', '17:30', 2, 'CR01'),
                        ('M006', 2, '2024-01-09', '11:00', 2, 'CR02'),
                        ('M007', 2, '2024-01-10', '17:00', 2, 'CR03'),
                        ('M008', 4, '2024-01-25', '18:30', 2, 'CR02'),
                        ('M009', 4, '2023-01-08', '13:00', 2, 'CR04'),
                        ('M010', 2, '2024-01-11', '14:00', 2, 'CR05'),
                        ('M011', 4, '2024-01-19', '15:30', 2, 'CR01'),
                        ('M012', 2, '2024-01-23', '15:00', 2, 'CR04');
                        ''')

        conn.execute('''INSERT INTO score
                VALUES  ('M001', 2, 0),
                        ('M002', 2, 1),
                        ('M003', 3, 2),
                        ('M004', 2, 0),
                        ('M005', 3, 1),
                        ('M006', 2, 0),
                        ('M007', '', ''),
                        ('M008', '', ''),
                        ('M009', '', ''),
                        ('M010', '', ''),
                        ('M011', '', ''),
                        ('M012', '', '');
                        ''')

        conn.execute('''INSERT INTO match_competitors
                VALUES  ('A00084', 'M001', '0'),
                        ('A00008', 'M001', '1'),
                        ('A00015', 'M002', '1'),
                        ('A00030', 'M002', '0'),
                        ('A00012', 'M003', '0'),
                        ('A00004', 'M003', '1'),
                        ('A00015', 'M004', '1'),
                        ('A00060', 'M004', '1'),
                        ('A00071', 'M004', '0'),
                        ('A00100', 'M004', '0'),
                        ('A00091', 'M005', '0'),
                        ('A00015', 'M005', '1'),
                        ('A00079', 'M006', '0'),
                        ('A00082', 'M006', '1'),
                        ('A00045', 'M007', '0'),
                        ('A00015', 'M007', '1'),
                        ('A00062', 'M008', ''),
                        ('A00075', 'M008', ''),
                        ('A00060', 'M008', ''),
                        ('A00091', 'M008', ''),
                        ('A00026', 'M009', ''),
                        ('A00013', 'M009', ''),
                        ('A00076', 'M009', ''),
                        ('A00015', 'M009', ''),
                        ('A00100', 'M010', ''),
                        ('A00046', 'M010', ''),
                        ('A00094', 'M011', ''),
                        ('A00078', 'M011', ''),
                        ('A00053', 'M011', ''),
                        ('A00004', 'M011', ''),
                        ('A00083', 'M012', ''),
                        ('A00057', 'M012', '');
                        ''')


def create_lessons():
        c5_advanced1_1 = ['A1_1', 'Monday', '10:00', '1', '4', 'C00005', 'CR01']
        c5_advanced1_2 = ['A1_2', 'Thursday', '10:00', '1', '4', 'C00005', 'CR01']
        c5_advanced2_1 = ['A2_1', 'Monday', '11:00', '1', '4', 'C00005', 'CR01']
        c5_advanced2_2 = ['A2_2', 'Thursday', '11:00', '1', '4', 'C00005', 'CR01']
        c5_advanced3_1 = ['A3_1', 'Monday', '12:00', '1', '4', 'C00005', 'CR01']
        c5_advanced3_2 = ['A3_2', 'Thursday', '12:00', '1', '4', 'C00005', 'CR01']
        c5_advanced4_1 = ['A4_1', 'Monday', '13:00', '1', '4', 'C00005', 'CR01']
        c5_advanced4_2 = ['A4_2', 'Thursday', '13:00', '1', '4', 'C00005', 'CR01']
        c10_special_needs1_1 = ['S1_1', 'Monday', '13:00', '1', '4', 'C00010', 'CR02']
        c10_special_needs1_2 = ['S1_2', 'Thursday', '13:00', '1', '4', 'C00010', 'CR02']
        c1_junior1_1 = ['J1_1', 'Monday', '14:00', '1', '8', 'C00001', 'CR03']
        c1_junior1_2 = ['J1_2', 'Thursday', '14:00', '1', '8', 'C00001', 'CR03']
        c2_junior2_1 = ['J2_1', 'Monday', '15:00', '1', '8', 'C00001', 'CR04']
        c2_junior2_2 = ['J2_2', 'Thursday', '15:00', '1', '8', 'C00001', 'CR04']
        c1_junior5_1 = ['J5_1', 'Monday', '14:00', '1', '8', 'C00002', 'CR03']
        c1_junior5_2 = ['J5_2', 'Thursday', '14:00', '1', '8', 'C00002', 'CR03']
        c2_junior6_1 = ['J6_1', 'Monday', '15:00', '1', '8', 'C00002', 'CR04']
        c2_junior6_2 = ['J6_2', 'Thursday', '15:00', '1', '8', 'C00002', 'CR04']
        c6_advanced5_1 = ['A5_1', 'Monday', '16:00', '1', '4', 'C00006', 'CR05']
        c6_advanced5_2 = ['A5_2', 'Wednesday', '16:00', '1', '4', 'C00006', 'CR05']
        c6_advanced6_1 = ['A6_1', 'Monday', '17:00', '1', '4', 'C00006', 'CR05']
        c6_advanced6_2 = ['A6_2', 'Wednesday', '17:00', '1', '4', 'C00006', 'CR05']
        c8_high_perf1_1 = ['P1_1', 'Monday', '17:00', '1.5', '4', 'C00008', 'CR06']
        c8_high_perf1_2 = ['P1_2', 'Wednesday', '17:00', '1.5', '4', 'C00008', 'CR06']
        c6_advanced7_1 = ['A7_1', 'Monday', '18:00', '1', '4', 'C00006', 'CR05']
        c6_advanced7_2 = ['A7_2', 'Wednesday', '18:00', '1', '4', 'C00006', 'CR05']
        c6_advanced8_1 = ['A8_1', 'Monday', '19:00', '1', '4', 'C00006', 'CR05']
        c6_advanced8_2 = ['A8_2', 'Wednesday', '19:00', '1', '4', 'C00006', 'CR05']
        c8_high_perf2_1 = ['P2_1', 'Monday', '19:00', '1.5', '4', 'C00008', 'CR06']
        c8_high_perf2_2 = ['P2_2', 'Wednesday', '19:00', '1.5', '4', 'C00008', 'CR06']
        c7_advanced9_1 = ['A9_1', 'Tuesday', '10:00', '1', '4', 'C00007', 'CR07']
        c7_advanced9_2 = ['A9_2', 'Thursday', '16:00', '1', '4', 'C00007', 'CR07']
        c7_advanced10_1 = ['A10_1', 'Tuesday', '11:00', '1', '4', 'C00007', 'CR07']
        c7_advanced10_2 = ['A10_2', 'Thursday', '17:00', '1', '4', 'C00007', 'CR07']
        c7_advanced11_1 = ['A11_1', 'Tuesday', '12:00', '1', '4', 'C00007', 'CR07']
        c7_advanced11_2 = ['A11_2', 'Friday', '12:00', '1', '4', 'C00007', 'CR07']
        c7_advanced12_1 = ['A12_1', 'Tuesday', '13:00', '1', '4', 'C00007', 'CR07']
        c7_advanced12_2 = ['A12_2', 'Friday', '13:00', '1', '4', 'C00007', 'CR07']
        c4_beginners5_1 = ['B5_1', 'Tuesday', '13:00', '1', '4', 'C00004', 'CR01']
        c4_beginners5_2 = ['B5_2', 'Thursday', '17:00', '1', '4', 'C00004', 'CR01']
        c4_beginners6_1 = ['B6_1', 'Tuesday', '14:00', '1', '4', 'C00004', 'CR01']
        c4_beginners6_2 = ['B6_2', 'Thursday', '18:00', '1', '4', 'C00004', 'CR01']
        c4_beginners7_1 = ['B7_1', 'Tuesday', '15:00', '1', '4', 'C00004', 'CR01']
        c4_beginners7_2 = ['B7_2', 'Thursday', '19:00', '1', '4', 'C00004', 'CR01']
        c4_beginners8_1 = ['B8_1', 'Tuesday', '16:00', '1', '4', 'C00004', 'CR01']
        c4_beginners8_2 = ['B8_2', 'Thursday', '20:00', '1', '4', 'C00004', 'CR01']
        c1_junior3_1 = ['J3_1', 'Tuesday', '17:00', '1', '8', 'C00001', 'CR02']
        c1_junior3_2 = ['J3_2', 'Friday', '17:00', '1', '8', 'C00001', 'CR02']
        c1_junior4_1 = ['J4_1', 'Tuesday', '18:00', '1', '8', 'C00001', 'CR02']
        c1_junior4_2 = ['J4_2', 'Friday', '18:00', '1', '8', 'C00001', 'CR02']
        c2_junior7_1 = ['J7_1', 'Tuesday', '17:00', '1', '8', 'C00002', 'CR03']
        c2_junior7_2 = ['J7_2', 'Friday', '17:00', '1', '8', 'C00002', 'CR03']
        c2_junior8_1 = ['J8_1', 'Tuesday', '18:00', '1', '8', 'C00002', 'CR03']
        c2_junior8_2 = ['J8_2', 'Friday', '18:00', '1', '8', 'C00002', 'CR03']
        c3_beginners1_1 = ['B1_1', 'Wednesday', '10:00', '1', '4', 'C00003', 'CR04']
        c3_beginners1_2 = ['B1_2', 'Friday', '12:00', '1', '4', 'C00003', 'CR04']
        c3_beginners2_1 = ['B2_1', 'Wednesday', '11:00', '1', '4', 'C00003', 'CR04']
        c3_beginners2_2 = ['B2_2', 'Friday', '13:00', '1', '4', 'C00003', 'CR04']
        c9_high_perf3_1 = ['P3_1', 'Wednesday', '11:00', '1.5', '4', 'C00009', 'CR05']
        c9_high_perf3_2 = ['P3_2', 'Friday', '10:00', '1.5', '4', 'C00009', 'CR05']
        c3_beginners3_1 = ['B3_1', 'Wednesday', '12:00', '1', '4', 'C00003', 'CR04']
        c3_beginners3_2 = ['B3_2', 'Friday', '14:00', '1', '4', 'C00003', 'CR04']
        c3_beginners4_1 = ['B4_1', 'Wednesday', '13:00', '1', '4', 'C00003', 'CR04']
        c3_beginners4_2 = ['B4_2', 'Friday', '15:00', '1', '4', 'C00003', 'CR04']
        c9_high_perf4_1 = ['P4_1', 'Wednesday', '13:00', '1.5', '4', 'C00009', 'CR05']
        c9_high_perf4_2 = ['P4_2', 'Friday', '19:00', '1.5', '4', 'C00009', 'CR05']
        c10_special_needs2_1 = ['S2_1', 'Wednesday', '15:00', '1', '4', 'C00010', 'CR06']
        c10_special_needs2_2 = ['S2_2', 'Friday', '16:00', '1', '4', 'C00010', 'CR06']

        courses = [c5_advanced1_1, c5_advanced1_2, c5_advanced2_1, c5_advanced2_2, c5_advanced3_1, c5_advanced3_2,
                c5_advanced4_1, c5_advanced4_2, c10_special_needs1_1, c10_special_needs1_2, c1_junior1_1,
                c1_junior1_2, c2_junior2_1, c2_junior2_2, c1_junior5_1, c1_junior5_2, c2_junior6_1, c2_junior6_2,
                c6_advanced5_1, c6_advanced5_2, c6_advanced6_1, c6_advanced6_2, c8_high_perf1_1, c8_high_perf1_2,
                c6_advanced7_1, c6_advanced7_2, c6_advanced8_1, c6_advanced8_2, c8_high_perf2_1, c8_high_perf2_2,
                c7_advanced9_1, c7_advanced9_2, c7_advanced10_1, c7_advanced10_2, c7_advanced11_1, c7_advanced11_2,
                c7_advanced12_1, c7_advanced12_2, c4_beginners5_1, c4_beginners5_2,c4_beginners6_1, c4_beginners6_2,
                c4_beginners7_1, c4_beginners7_2, c4_beginners8_1, c4_beginners8_2, c1_junior3_1, c1_junior3_2,
                c1_junior4_1, c1_junior4_2, c2_junior7_1, c2_junior7_2, c2_junior8_1, c2_junior8_2, c3_beginners1_1,
                c3_beginners1_2, c3_beginners2_1, c3_beginners2_2, c9_high_perf3_1, c9_high_perf3_2, c3_beginners3_1,
                c3_beginners3_2, c3_beginners4_1, c3_beginners4_2, c9_high_perf4_1, c9_high_perf4_2, c10_special_needs2_1,
                c10_special_needs2_2]
        week = []
        day_i = today

        for course in courses:
                conn.execute('''INSERT INTO course VALUES(?,?,?,?,?,?)''',
                             (course[0], course[1], course[2], course[3], course[4], course[5]))

        for i in range(7):
                week.append(day_i)
                day_i = day_i + timedelta(days=1)

                date_of_week = datetime.strptime(str(week[i]), "%Y-%m-%d")
                day_of_week = date_of_week.strftime('%A')

                for course in courses:
                        if day_of_week == course[1]:
                                cur.execute("SELECT max(lessonID) FROM lesson")
                                lessonid = cur.fetchone()
                                if lessonid[0] == None:
                                       lessonid = "L001"
                                else:
                                        lessonid = increase(lessonid)

                                conn.execute('''INSERT INTO lesson VALUES(?,?,?,?,?,?,?)''',
                                        (lessonid, course[0], week[i], course[2], course[3], course[6], None))


def fill_courses():
        cur.execute("SELECT memberID FROM member WHERE memberID IN "
                "(SELECT athID FROM athlete WHERE pack_end_date >= CURRENT_DATE)")
        athleteIDs = cur.fetchall()
        athletes = []
        for id in athleteIDs:
                athletes.append(id[0])

        cur.execute("SELECT courseID FROM course")
        courseIDs = cur.fetchall()
        allcourses = []
        for id in courseIDs:
                allcourses.append(id[0])

        for athlete in athletes:
                courses = allcourses
                cur.execute("SELECT Level FROM athlete WHERE athID = '" + athlete + "';")
                level = cur.fetchone()[0]
                if level == 'advanced' or level == 'advanced intermediate':
                        courses = [s for s in courses if s.startswith('A') and s.endswith('1')]
                if level == 'beginner' or level == 'intermediate':
                        courses = [s for s in courses if s.startswith('B') and s.endswith('1')]
                if level == 'junior':
                        courses = [s for s in courses if s.startswith('J') and s.endswith('1')]
                if level == 'professional':
                        courses = [s for s in courses if s.startswith('P') and s.endswith('1')]
                if level == 'special needs':
                        courses = [s for s in courses if s.startswith('S') and s.endswith('1')]
                #print(courses)
                course = courses[0]
                i = 0
                while True:
                        #print(course)
                        cur.execute("SELECT COUNT(athID) FROM athlete_course GROUP BY courseID HAVING courseID = '"+ course +"';")
                        num_athletes = cur.fetchone()
                        #print(num_athletes)
                        if num_athletes == None:
                                num_athletes = (0,)
                        cur.execute("SELECT no_of_participants FROM course WHERE courseID = '"+ course +"';")
                        max_participants = cur.fetchone()
                        if num_athletes[0] == max_participants[0]:
                                i = i + 1
                                course = courses[i]
                                continue
                        else:
                                break
                conn.execute('''INSERT INTO athlete_course VALUES (?,?)''', (athlete, course))
                prefix = course[:-1]
                new_number = '2'
                course_2 = f"{prefix}{new_number}"
                conn.execute('''INSERT INTO athlete_course VALUES (?,?)''', (athlete, course_2))

def fill_database():
        upload_data()
        create_lessons()
        fill_courses()
        conn.commit()
        print("Data succesfully loaded.")

if __name__ == "__main__":
    fill_database()
    conn.close()



# import pickle
# # imelad = ('More mayhem',
# #           'Imelda may',
# #           '2011',
# #           (1,'Pulling the rug'),
# #           (2,'Psycho'),
# #           (3,'Mayhem'),
# #           (4,'Kentish Town Waltz')
# #           )
# # with open("imelad.pickle",'wb') as pickle_file:
# #     pickle.dump(imelad,pickle_file)
# with open('imelad.pickle','rb') as pickle_files:
#     imelda2 = pickle.load(pickle_files)
# print(imelda2)
# album,artist,year= imelda2
# print(album,'\n',artist,'\n',year,'\n')
# for track in track_list:
#     track_number,track_title = track
#     print(track_number,track_title)
import pickle

imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1,'Pulling the rug'),
           (2,'Psycho'),
           (3,'Mayhem'),
           (4,'Kentish Town Waltz')))
even = list(range(0,10,2))
odd = list(range(1,10,2))
with open("imelda.pickle",'wb') as picle_files:
    pickle.dump(imelda,picle_files)
    pickle.dump(odd,picle_files)
    pickle.dump(even,picle_files)
    pickle.dump(77777,picle_files)
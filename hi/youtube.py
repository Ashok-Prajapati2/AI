from youtubesearchpython import *

customSearch = CustomSearch('N', VideoSortOrder.uploadDate, limit = 1)

print(customSearch.result())
from object_error import ErrorKangaroo

kanga = ErrorKangaroo('Kanga')
roo = ErrorKangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)

# If you run this program as is, it seems to work.
# To see the problem, trying printing roo.

print(roo)
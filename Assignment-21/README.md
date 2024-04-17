# Assignment-21
---
## Shop With SQLite3(main.py)
> [!NOTE]
This is a shop program that execute in terminal.

> [!IMPORTANT]  
This program CREATE, READ, UPDATE and DELETE (CRUD) products in database by using SQLite3.

![shop program](./1.JPG)

---
## Music maker
> [!NOTE]
This program making music by PySynth library.

> [!IMPORTANT]
wirte notes in the form of tuples.first member is note name like: "C" for 'do', "D" for 're', "E" for 'mi', "F" for 'fa', "G" for 'sol', "A" for 'la', "B" for 'si' and second member is note duration like 'Harp note' and export a WAV file.

> [!TIP]
1. first `import pysynth_b`
2. write note, for example : 
`song = (('c', 6),('d', 6),('e', 6),('e', 6),
        ('e', 6),('e', 6),('e', 6),('g', 6),('e', 3),
        ('e', 6),('g', 6),('e', 6), ('g', 6),('e', 3),
        ('e', 6),('f', 6),('d', 6),('e', 6),('c', 3),
        ('d', 6),('e', 6),('d', 6),('e', 6),('c', 3),
        ('c', 6),('d', 6),('c', 6),('d', 6),('c', 3),
        ('g', 6),('f', 6),('e', 6),('f', 6),('e', 3))`
3.use `make_wav(song, fn = "song.wav", leg_stac = .7, bpm = 180)` to make ouutput wav file.
![PySynth](./2.JPG)

; Damian Kokot
; nasm -f elf indeks.asm && ld -m elf_i386 -s -o indeks indeks.o
; Tworzenie podciągu do zadania 2.1 objdump -d indeks

[SECTION .text]

global _start

_start:
        call starter	; dodajemy na stos numer indeksu
        db '250089'

        starter:
        xor eax, eax    ; Zerujemy rejestry
        xor ebx, ebx
        xor edx, edx
        xor ecx, ecx

        mov al, 4       ; komenda wypisywania
        mov bl, 1       ; kod IO na stdout to 1
        pop ecx         ; zdejmujemy ze stosu adres na numer indeksu
        mov dl, 6       ; długość indeksu 
        int 0x80

        xor eax, eax
        xor ebx,ebx
        mov al, 1       ; Koniec
        int 0x80

// Damian Kokot
// gcc smartnot.c -o smartnot -m32 -fno-stack-protector -z execstack

#include <unistd.h>

char shellcode[] = "\xe8\x06\x00\x00\x00\x32\x35\x30\x30\x38\x39\x31\xc0\x31\xdb\x31\xd2"\
                    "\x31\xc9\xb0\x04\xb3\x01\x59\xb2\x06\xcd\x80\x31\xc0\x31\xdb\xb0\x01\xcd\x80";

int main(int argc, char* argv[]) 
{
  int *ret;
  ret = (int *)&ret + 2;
  (*ret) = (int) shellcode;
}

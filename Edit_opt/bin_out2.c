#include <stdio.h>
#include <stdlib.h>
/*
int main(void)
{
    char *data = "11111111";
    char c = strtol(data, 0, 2);
    printf("%s = %c = %d = 0x%.2X\n", data, c, c, c);
    return(0);
}*/
int main()
{
FILE *stream;
stream = fopen("samp_bin.bin","wb");
unsigned int intval = 0b11111111;       
unsigned char charval = intval;
fwrite (&charval, 1, 1, stream);
fclose(stream);
FILE *st;
st = fopen("samp_bin.bin","rb");
//unsigned int intval = 0b11111111;       
unsigned char cval;
fread (&cval, 1, 1, st);
printf("%c",cval);
fclose(st);
}
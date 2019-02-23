#include <stdio.h>
#include <stdlib.h>
#include<string.h>
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
int i,j=0, n=2; 
char ch;

char *str = NULL;
size_t len = 0;
ssize_t read;
FILE *fp = fopen("samp_inp.txt", "r");

FILE *fptr;
fptr = fopen("samp_bin.bin","a+");

unsigned int intval = 0b00000000;       
unsigned char charval;

if (fptr == NULL) 
{ 
    printf("Could not open file"); 
    return 0; 
}
while((read=getline(&str, &len, fp))!=-1)
{
for(i=0;i<=strlen(str);i++)
{
    ch = toupper(str[i]);
    switch(ch)
    {
        case 'A':
            intval = intval << 2;
            intval = intval + 0b00000000;
            break;
        case 'C':
            intval = intval << 2;
            intval = intval + 0b00000001;
            break;
        case 'G':
            intval = intval << 2;
            intval = intval + 0b00000010;
            break;
        case 'T':
            intval = intval << 2;
            intval = intval + 0b00000011;
            break;
    }
    j++;
    if(j==3)
    {
        
        charval = intval;
        fwrite (&charval, 1, 1, fptr);
        intval = 0b00000000;
        j=0;

    }
    
}
}

//fwrite (&charval, 1, 1, stream);
fclose(fptr);
fclose(fp);



/*
FILE *st;
char *strn = NULL;
size_t len1 = 0;
ssize_t read1;
st = fopen("samp_bin.bin","rb");
//unsigned int intval = 0b11111111;       
unsigned char cval;
while((read1=getline(&strn, &len1, st))!=-1)
{
 printf("%s",strn);
}
//fread (&cval, 1, 2, st);
//printf("%d",cval);
fclose(st);
*/
unsigned char buffer[24];
FILE *ptr;

ptr = fopen("samp_bin.bin","rb");  // r for read, b for binary

fread(buffer,1,1,ptr);
for(int i = 0; i<8; i++)
    printf("%d ", buffer[i]);
}


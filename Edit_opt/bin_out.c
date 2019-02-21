#include<stdio.h> 
#include <string.h>
#include <ctype.h>
#include<stdlib.h>
main() 
{ 
    int i, n=2; 
    char ch;
    //char str[81]="AATATTACAGAAAAATCCCCACAAAAATCacctaaacataaaaatattctacttttcaacaataataCATAAACATATTG";
    char *str = NULL;
	size_t len = 0;
	ssize_t read;

    FILE *fp = fopen("samp_inp.txt", "r");

    FILE *fptr = fopen("samp_bin.bin", "wb"); 
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
                fprintf(fptr,"00");
                break;
            case 'C':
                fprintf(fptr,"01");
                break;
            case 'G':
                fprintf(fptr,"10");
                break;
            case 'T':
                fprintf(fptr,"11");
                break;
        }

    }
    }
    //fprintf(fptr,"11011011"); 
    free(str);
    fclose(fptr);
    
    //FILE *fp;
   //char c[] = "this is tutorialspoint";
   //char buffer[8];

   /* Open file for both reading and writing */
   //fp = fopen("samp_bin.bit", "r");

   /* Write data to the file */
   //fwrite(c, strlen(c) + 1, 1, fp);

   /* Seek to the beginning of the file */
   //fseek(fp, 0, SEEK_SET);

   /* Read and display data */
   //fread(buffer, 8, 1, fp);
   //printf("%s\n", buffer);
   //fclose(fp);
     
} 

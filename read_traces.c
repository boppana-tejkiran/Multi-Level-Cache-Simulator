#include<stdio.h>
#include<assert.h>
#include<stdlib.h>
#include<string.h>

void main(int argc, char* argv[]){
   FILE *fp, *wp;
   wp=fopen("sample.txt","w");
   int numtraces = atoi(argv[2]);
   int k;
   char input_name[40];
   char iord,type;
   unsigned pc;
   unsigned long long addr;
   for (k=0; k<numtraces; k++) {
      sprintf(input_name, "%s_%d", argv[1], k);
      fp = fopen(input_name, "rb");
      assert(fp != NULL);

      while (!feof(fp)) {
         fread(&iord, sizeof(char), 1, fp);
         fread(&type, sizeof(char), 1, fp);
         fread(&addr, sizeof(unsigned long long), 1, fp);
         fread(&pc, sizeof(unsigned), 1, fp);
         if(type)
            fprintf(wp, "%llu\n", addr);
      }
      fclose(fp);
      printf("Done reading file %d!\n", k);
   }
   fclose(wp);
}



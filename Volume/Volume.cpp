#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define PI 3.141592
float 	pide();
float area (float r);
void area(); 
void imprime (float);

main()
{
      int dec, elec;
      float Vci, Vco, r,h, ar;
      do
	  {
		printf("Hola\n");
      printf("Do you want to calculate the volume of...? 1)Cylinder 2)Cone");
      scanf("%i",&dec);
      printf("Write the value of the radius");
      scanf("%f",&r);
      ar=area(r);
    
      if(dec==1)
      {
        h=pide();
        Vci=ar*h;
        imprime(Vci);
       }
       else 
       {
       	h=pide();
    	Vco=(Vci)/3;
        imprime(Vco);
		}                         
      printf("Do you want to calculate another volume? 1)Yes 2)No");
      scanf("%i",&elec);
      }
	  while (elec==1);
	  system("PAUSE");
      system("cls");
      printf("A La Gloria Del Gran Arquitecto Del Universo\n");
      system("PAUSE"); 
}

float pide()
{
      float h;     
      printf("Write the value of the height");
      scanf("%f",&h);
      return h;
}

float area(float r)
{
     float area2;
     area2=PI*r*r;
     return area2;
}

void imprime (float Vol)
{
     printf("The volume of the figure is %f ", Vol);
 }

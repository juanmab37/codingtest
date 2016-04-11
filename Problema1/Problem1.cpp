// Baruffaldi Juan Manuel
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX 1000

bool IsPrime(long long n) //Determina si un numero es primo o no
{
	if (n < 2) 	return false;
	if (n < 4) return true;
	if (n % 2 == 0)return false;
	
	const long long iMax = (long long)sqrt(n) + 1;
	long long i;
	for (i = 3; i <= iMax; i += 2)
		if (n % i == 0)
			return false;
		
	return true;
}

int * suma_array(int *a, int *b,int la, int lb, int *lc) //opera sobre arrays de Int
{
	int *c,na,nb,i,*r;
	
	c=(int*)malloc(sizeof(int)*(la*2));
	*lc=i=0;
	la--;
	lb--;
	
	while(la>=0 || lb>=0){
		na=nb=0;
		if(la>=0){
			na=a[la];
		}
		if(lb>=0){
			nb=b[lb];
		}
		c[*lc]=na+nb;
		(*lc)++;
		la--;
		lb--;
	}
	
	while(i<(*lc)-1){
		if(c[i]>9){
			c[i+1]++;
			c[i]=c[i]%10;
		}
		i++;
	}
	
	if(c[i]>9){
		c[i+1]=1;
		c[i]=c[i]%10;
		(*lc)++;
	}
	
	nb=*lc-1;
	
	r=(int*)malloc(sizeof(int)*(*lc));
	
	for(i=0;i<*lc;i++){
		r[i]=c[(*lc-1)-i];
	}
	
	nb=*lc-1;
	
	free(c);
	
	return r;
}

long double fib_n2(int n) //Otra forma de calcular fibonacci
{
	long double res=0;
	double raiz5 = sqrt(5);
	long double a = pow((1+raiz5)/2.0,n);
	long double b = pow((1-raiz5)/2.0,n); 
	res = (1.0/raiz5)*( a - b);

	return res;
}

bool detFibPrim(int n) //Determina si dado un numero n, fib n es primo
{
	int *fn,*fa,*fp;
	int lp,la,ln,i;
	
	fn=(int *)malloc(sizeof(int)*MAX);
	fa=(int *)malloc(sizeof(int)*MAX);
	fp=(int *)malloc(sizeof(int)*MAX);
	
		
	fa[0]=1;
	fp[0]=1;
	lp=la=ln=1;
	
	for(i=3;i<=n;i++){
		fn=suma_array(fa,fp,la,lp,&ln);
		fp=fa;
		lp=la;
		fa=fn;
		la=ln;
		
		/*for(int j=0;j<ln;j++){
			printf("%d",fn[j]);
		}
		printf("\n");*/
	}
//	printf("Fn(%d)= ",n);
	if(n==1){
	//	printf("1\n");
		fn[0] = 1;
	}else if(n==2){
		//printf("1\n");
		fn[0] = 1;
	}else{
		for(i=0;i<ln;i++){
			//printf("%d",fn[i]);
		}
		//printf("\n");
	}
	
	long double fibn_d=0;
	
	for(int i=ln-1; i>=0; i--){
		//printf("fn[%d] = %d\n",i,fn[i]);
		fibn_d += fn[i]*pow(10, ln -1 - i);
		//printf("pow(10,%d) = %f\n",ln -1 - i,pow(10, ln -1 - i));
	}
	
	long long fibn=fibn_d;
	//printf("Fib %lld\n",fibn);
	
	if(IsPrime(fibn))
	{
		//printf("Es primo\n");
		return true;
	}
	else
		//printf("No primo\n");
		
	return false;
}

void respuestaA()
{
	int primos[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89}; //Esto se demostro matematicamente
	int cnt_p=24;
	
	printf("Respuesta A: ");
	for(int i=0; i<cnt_p; i++)
	{
		if(detFibPrim(primos[i]))
			printf("%d, ",primos[i]);
	}
	
	//A esta solucion se le debe agregar el 4 ya que es la excepción a la regla matematica
	printf("4");
	
	printf("\n");
}
	
int respuestaB(int n) //Devuelve la cantidad de cifras al calcular un número de Fibonacci
{
	int *fn,*fa,*fp;
	int lp,la,ln;
	
	fn=(int *)malloc(sizeof(int)*MAX);
	fa=(int *)malloc(sizeof(int)*MAX);
	fp=(int *)malloc(sizeof(int)*MAX);
		
	fa[0]=1;
	fp[0]=1;
	lp=la=ln=1;
	
	for(int i=3;i<=n;i++){
		fn=suma_array(fa,fp,la,lp,&ln);
		fp=fa;
		lp=la;
		fa=fn;
		la=ln;
	}
		
	return ln;
}
	

int main(int argc, char **argv)
{
	
	respuestaA();
		
	printf("Cantidad de Cifras de Fib(1477): %d\n",respuestaB(1477));
	

	
	return 0;
}
	

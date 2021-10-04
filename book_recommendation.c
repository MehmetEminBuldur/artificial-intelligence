//Book recommandation system with pearson coefficient//
//						     //


#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int finduser(char *u,char **users){//kullanici listesinden kullanicinin indexini bulma islemi
	int i=0;
	while(users[i][0]!='\0'){
		if(strcmp(u,users[i])==0){
			return i;
		}
		i++;
	}
	return -1;
}
float *similarity(char *u1,char **users,int **points,int bc){//bc kitap sayisi,points puanlar, users kullanici isimleri,u1 test kullanicisi
	float *simarr;//similarity array
	simarr=(float*)malloc(50*sizeof(float));
	int ix=finduser(u1,users);//kullanicinin indexini bulma islemi
	int i=0;
	int j;
	if(ix==-1){//eger kullanici bulunamadiysa 
		printf("Hatali Kullanici Adi!!");
		return -1;
	}
	float ra=0,rb=0,x,y,xy=0,x2=0,y2=0,result;//ra,rb ortak okunan kitaplar icin ortalamalar, rap,rbp o kitaba verilen puanlar
	int oks;//okunmus kitap sayisi
	while(users[i][0]!='\0'){//kullanicilar icinde gezinme ve her kullanici icin benzerlik hesaplamasi
		ra=0;rb=0;x2=0;y2=0;xy=0;//denklemde kullanilacak degerlerin 0'lanmasi
		if(i==ix){// eger test kullanicisina gelindiyse benzerlik 0 olarak giriliyor
			simarr[ix]=0;
		}else{
			oks=0;
			for(j=0;j<bc;j++){// ra ve rb degerleri hesaplama
				if(points[i][j]!=0&&points[ix][j]!=0){
					ra=ra+(float)points[ix][j];
					rb=rb+(float)points[i][j]; 
					oks++;
				}
			}
			ra=ra/(float)oks;
			rb=rb/(float)oks;
			for(j=0;j<bc;j++){//denklem islemleri
				if(points[i][j]!=0&&points[ix][j]!=0){
					x=(float)points[ix][j]-ra;
					y=(float)points[i][j]-rb;
					xy=xy+x*y;
					x2=x2+x*x;
					y2=y2+y*y;
				}
			}
			result=xy/(sqrt(x2)*sqrt(y2));
			simarr[i]=result;//sonuc
		}
		i++;
	}
	return simarr;
}
float *pred(int **points,int ui1,float *simarr,int n,int *a,int k,int bc){//points-->puanlar matrisi,ui1-->test kullanicisi indexi,
	int i;//similariy dizisinde gezimek icin 							  //simarr-->similarity array,n-->ogrenmne yapilacak kullanici sayisi
	int j;//en yakin k kullaniciyi tutan diziyi bulmak icin				  //a-->max similarity dizisi,k-->(k=2,3,4..),bc-->book count
	int m;//en yakin kullanicilar dizisinde(a[]) arama yapmak icin
	int max;//dizide max elemani tutmak icin
	float *pred;//tahmin degerlerinin tutuldugu dizi
	pred=(float*)malloc(50*sizeof(float));
	for(j=0;j<k;j++){//en yakin kullanicilar dizisine k kadar en yakin(max similarity) kullaniciyi ekleme islemi
		max=0;
		for(i=0;i<n;i++){
			if(simarr[i]>simarr[max]){
				m=j;
				while(m>=0&&i!=a[m]){
					m--;
				}
				if(m<0){//max dizisinde bulunamadi demek
					max=i;
				}
			}	
		}
		a[j]=max;
	}
	float ra=0;
	float rb=0;
	float predsum=0;//denklemde hesaplama yapmak icin 
	float simsum=0;//denklemde hesaplama yapmak icin 
	int oks;//ortak okunan kitap sayisi
	int x=0;//tahmin degerlerini diziye kayit icin
	int b;//kitap puanlari arasinda gezinmek icin
	for(b=0;b<bc;b++){//degeri 0 olan kitaplarin tahmin degerlerini hesaplama islemi
		if(points[ui1][b]==0){
			predsum=0;
			simsum=0;
			for(j=0;j<k;j++){
				ra=0;rb=0;oks=0;
				for(i=0;i<bc;i++){
					ra=ra+(float)points[ui1][i];
					rb=rb+(float)points[a[j]][i];
					oks++;
				}	
				ra=ra/(float)oks;
				rb=rb/(float)oks;
				predsum=predsum+simarr[a[j]]*((float)points[a[j]][b]-rb);
				simsum=simsum+simarr[a[j]];
			}
			pred[x]=ra+(predsum/simsum);
			x++;
		}
	}
	return pred;
}
int main(){
	char line[300];//dosyadan satir satir veri okumak icin 
	int d;//donguler icin index
	char user[10];//kullanici adi kayit icin
	char **users=(char**)malloc(50*sizeof(char*));//
	for(d=0;d<50;d++){							  //
		users[d] = (char*)malloc(10*sizeof(char));//
	}           								  //bellek allokasyonlari
	char book[50];								  //
	char **books=(char**)malloc(50*sizeof(char*));//
	for(d=0;d<50;d++){							  //	
		books[d] = (char*)malloc(50*sizeof(char));//
	}
	char username[10];//kullanici adini kullanicidan almak icin
	int ky;//en yakın kullanicilarin sayisi(k=1,2,3,4...)
	printf("Kitap onerisi yapilacak kullanici adi: ");
	scanf("%s",username);
	printf("Benzer Kullanici Sayisi(k): ");
	scanf("%d",&ky);
	FILE *fp1;	
	if ((fp1 = fopen("recdataset.csv", "r" )) == NULL) {
		printf("Could not open the input file\n"); return 0;
	}
	fgets(line,300,fp1);//ilk satiri alip kitap isimlerini kayit icin
	int k=0;//satirda gezinme icin
	while(line[k]!=';'){//ilk satir ilk sutun(users) atlama islemi
		k++;
	}
	k++;
	int i=0;//kitaplar listesi icin
	int j=0;//kitap ismi harf harf kayit icin
	while(line[k]!='\0' && line[k]!='\n'){//kitap isimlerini string sizisi halinde tutma islemi
		if(line[k]==';'){//veri kutucugu bitisi
			book[j]='\0';//ismin bittigini belirtmek icin
			strcpy(books[i],book);//isim listesine kayit 
			i++;
			k++;
			j=0;
		}else if(line[k+1]=='\0' || line[k+1]=='\n'){//satir bitisi 
			book[j]=line[k];
			j++;
			book[j]='\0';
			strcpy(books[i],book);
			k++;
		}else{//harf kayit 
			book[j]=line[k];
			j++;
			k++; 
		}
	}
	int bcount=i+1;//kitap sayisi
	i=0;
	int **points=(int**)malloc(50*sizeof(int*));//puanlar matrisi ve bellek allokasyonu
	for(d=0;d<50;d++){
		points[d] = (int*)malloc(50*sizeof(int));
	};
	int uc=0;//u1,2,3,.... sayaci
	int nc=0;//nu1,2,3... sayaci
	while(fgets(line,300,fp1)!=NULL){//satir satir okuma ve kullanici adlari ve puanlari dizilere kayit islemi
		k=0;//satirda gezinmek icin
		j=0;//kullanici adi kaydetmek icin
		while(line[k]!=';'){//kullanici adi kayit
			user[j]=line[k];
			k++;
			j++;
		}
		if(user[0]=='U'){//u ile baslayanlari sayma, yani ögrenme verisi
			uc++; //u count
		}else{//nu'lari sayma , test verisi 
			nc++;// nu count 
		}
		user[k]='\0';
		strcpy(users[i],user);//kullanici adini string dizisine ekleme islemi
		j=0;//puan kaydetmek icin
		while(line[k]!='\0' && line[k]!='\n'){//puanlari kayit islemi
			if(line[k]==';'){
				if(line[k+1]==';'){
					points[i][j]=0;
					j++;
				}
				k++;
			}else{
				if(line[k]==' '){
					points[i][j]=0;
					k++;
					j++;
				}else{
					points[i][j]=line[k]-'0';
					k++;
					j++;
				}
			}
		}
		i++;
	}
	users[i][0]='\0';//siniri belirlemek icin
	float *sims;// similarity dizisi(degerlerin tumunun bulundugu dizi)
	sims=similarity(username,users,points,bcount);
	int z;//ekrana tahminleri basmak icin
	int *maxsimi;//max similarity indexleri(en yakin k icin)
	maxsimi=(int*)malloc(3*sizeof(int));
	float *predicts;//tahmin degerlerini kayit icin
	predicts=pred(points,finduser(username,users),sims,uc,maxsimi,ky,bcount);
	printf("%s kullanicisina en yakin kullanicilar(k=%d) ve hesaplanan pearson benzerlikleri sirasiyla,\n",username,ky);
	for(d=0;d<ky;d++){
		printf("%s, %f\n",users[maxsimi[d]],sims[maxsimi[d]]);//user ve similarity degerlerini ekrana basma
	}
	printf("%s kullanicisinda okunmamis olan kitaplar icin hesaplanan tahmini begenme degerleri:\n",username);
	d=0;
	int mx=0;
	int z1=0;
	for(z=0;z<bcount;z++){
		if(points[finduser(username,users)][z]==0){
			if(d==0){z1=z;}
			printf("%s, %f\n",books[z],predicts[d]);//kitap ve tahminleri ekran basma 
			if(predicts[mx]<predicts[d]){// tahmin degeri en buyuk olan kitabi bulma islemi
				mx=d;//normal max bulma islemi
				z1=z;//kitap isminin indexini tutma islemi
			}
			d++;
		}
	}
	printf("Sonuc olarak onerilen kitap: %s",books[z1]);
	free(books);
	free(users);
	free(points);
	fclose(fp1);
	return 0;
}

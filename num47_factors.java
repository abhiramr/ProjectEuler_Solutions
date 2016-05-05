import java.util.*;

class factors
{
	public boolean isPrime(int n)
	{
		int flag = 0;
		for(int i=2;i<n;i++)
		{
			if(n%i==0)
			{
				flag=1;
				break;
			}
		}
		if(flag==1) return false;
		return true;
	}
	public int factor(int n)
	{
		int i=1;
		int count=0;
		for(i=2;i<=(n);i++)
		{
			if(n%i==0)
			{
				
				if(isPrime(i))
				{
				//System.out.println(i);
				count++;
				}


			}
		}
		return count;
	}

	public static void main(String [] args)
	{

		int a,b,c,d,e,f,g,h;
		factors ob = new factors();

		for(int i=100000;i<200000;i++)
		{

			a=i-3;
			b=i-2;
			c=i-1;
			d=i;
			e=ob.factor(a);
			f=ob.factor(b);
			g=ob.factor(c);
			h=ob.factor(d);
			//System.out.println(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h);
			if(e==f && f==g && g==h && g==4)
			{
				System.out.println(a+" "+b+" "+c+" "+d);
			}



		}
	}

}
while (k<m && l<n)
{
	for(i=1;i<n;i++)
	{
		a[k][i] = a[x];
		x++;
	}
	k++;
	for (i=k ; i<m;i++)
	{
		a[i][n-1] =a[x];

		x++;
	}
	n--;
	if(k<m)
	{
		for (i=n-1;i<m ;i++ ) {
			arr[i][n-1] = a[x];
			x++;			
		}
		n--;
		if(k<m)
		{
			for (i=n-1;i>=1 ;--i ) {
				arr[m-1][i]= a[x];
				x++;
			}
			m--;
		}
		if(l<n)
		{
			for(i=m-1;i>=k;--i){
				arr[i][l] = a[x];
				x++;
			}
			l++;
		}
	}
}
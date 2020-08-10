import allel
import sqlite3
import pandas 
import numpy as  np
import sys
import io


def match_barcode(barcode):
	cladestring=np.array(['S','V','G','I','D'])
	matchmatrix=np.array(
	[['X','X','X','X','X','X','X','X','X','X','X'],
	['X','X','X','X','X','X','X','X','X','X','X'],
	['X','X','X','X','X','X','X','X','X','X','X'],
	['X','X','X','X','X','X','X','X','X','X','X'],
	['X','X','X','X','X','X','X','X','X','X','X']]
	)
	clade=np.array(
	[['T','C','G','C','C','C','A','G','T','G','G'],
	['C','T','T','C','C','C','A','G','T','G','G'],
	['C','T','G','T','T','T','G','G','T','G','G'],
	['C','T','G','C','C','C','A','A','C','G','G'],
	['C','T','G','C','C','C','A','A','C','A','A']]
	)
	score=np.array([0,0,0,0,0])
	cladeindex=0
	for bc in clade:
		matchcount=0
		i=0
		for b in bc:
			if(b==barcode[i]):
				matchcount=matchcount+1
				matchmatrix[cladeindex][i]='|'
			i=i+1	
		score[cladeindex]=matchcount
		cladeindex=cladeindex+1
	max_index = np.argmax(score, axis=0)
	print()
	print("Sample",barcode)
	print("Match ",matchmatrix[max_index])
	print("Clade %s"%(cladestring[max_index]),end="")
	print(clade[max_index])
	print("Clade %s matches %3.0f%%  "%(cladestring[max_index],(score[max_index]*100/11)))

	
#callset = allel.read_vcf('calls.vcf',numbers={'ALT': 100})
callset = allel.read_vcf(sys.stdin.buffer.raw,numbers={'ALT': 100})
positions=callset['variants/POS']
alt=callset['variants/ALT']
ref=callset['variants/REF']
samples=callset['samples']
calls=callset['calldata/GT']
chrom=callset['variants/CHROM']
samplecode={}
i=0
for p in positions:
	r=ref[i]
	a=alt[i,calls[i,0,0]-1]
	samplecode[p]=a
	i=i+1

print(samplecode)
barcode=np.array(['C','T','G','C','C','C','A','G','T','G','G'])
barcode[0]=samplecode.get(8782,'C')
barcode[1]=samplecode.get(28144,'T')
barcode[2]=samplecode.get(26144,'G')
barcode[3]=samplecode.get(241,'C')
barcode[4]=samplecode.get(3037,'C')
barcode[5]=samplecode.get(14408,'C')
barcode[6]=samplecode.get(23403,'A')
barcode[7]=samplecode.get(1397,'G')
barcode[8]=samplecode.get(28688,'T')
barcode[9]=samplecode.get(1440,'G')
barcode[10]=samplecode.get(2891,'G')

match_barcode(barcode)


#for p in positions:
#    for s in range(0,len(samples)):
#        if(calls[i,s,0]>0):
#            r=ref[i]
#            a=alt[i,calls[i,s,0]-1]
#            lr=len(r)
#            la=len(a)
#            mtype='S'
#            m=max(lr,la)-1
#            if(lr>la):
#                mtype='D'
#            elif(lr<la):
#                mtype='I'
#            else:
#                mtype='S'
#                m=1
#            print(chrom[i],p,p+m-1,samples[s],r,a,mtype,m)
#    i=i+1
#
#

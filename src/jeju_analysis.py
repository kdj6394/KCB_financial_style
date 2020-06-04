from lib import os,glob,sys,join,basename,dirname
from lib import np,pd,plt,sns
plt.rc('font',family='Malgun Gothic')
from lib import warnings
warnings.filterwarnings(action='ignore')

if __name__ == '__main__':
    root = sys.argv[1]
    csv_name = 'jeju_financial_life_data.csv'
    
    csv_file = join(root,csv_name)
    data = pd.read_csv(csv_file,encoding='utf-8')
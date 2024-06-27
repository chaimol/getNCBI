#输入一列SRR的编号，输出是ascp的下载脚本


if [ -z $1 ];then
	echo "
	用于获取SRR的下载命令
	Usage:$0 SRRlistfile
	输入一列SRR的编号，输出是ascp的下载脚本
	"
	exit 1
fi

SRRfile=$1

cat SRRfile|awk '{print substr($1,1,6)}' >left
cat SRRfile|awk '{print "00"substr($1,10,10)}' >end
paste -d "/" left end ${SRRfile} ${SRRfile} >meg

awk '{print "ascp -QT -l 300m -P33001 -i $HOME/.aspera/connect/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/"$0"_1.fastq.gz ."}' meg >fq_1
awk '{print "ascp -QT -l 300m -P33001 -i $HOME/.aspera/connect/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/"$0"_2.fastq.gz ."}' meg >fq_2
cat fq_1 fq_2 >download.bash
echo "输出的下载命令文件是download.bash"
rm -rf lef end meg fq_1 fq_2

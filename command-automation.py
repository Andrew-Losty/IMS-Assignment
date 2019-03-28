#import python components
Import os
From datetime import datetime

#show current working directory
print(os.getcwd())


#change cwd to C:\temp					
os.chdir('/temp')


#show contents of C:\temp					
print(os.lstdir())	

#make directory C:\temp\demo/sub-demo					
os.makedirs('demo/sub-demo')	

#remove directory C:\temp\demo/sub-demo			
os.removedirs('demo/sub-demo')

#rename file original.txt to new.txt			
os.rename(‘original.txt, ‘new.txt’)			

#show modification time for file new.txt
mod_time = os.stat('new.txt').st_mytime		
print (datetime.fromtimestamp(mod_time))

#show entire directory tree
for dirpath, dirnames, filenames in os.walk(‘/temp’):		
    print('Current Path:' , dirpath)
    print('Directories:',dirnames)
    print('Files:', filenames)
    print()	

Environment Variables
print(os.environ())
print(os.environ.get('COMPUTERNAME'))
print(os.environ.get('HOMEPATH'))
file_path = os.path.join(os.environ.get(‘HOMEPATH’, ‘test.txt)

#Use of Python to automate the generation of stream files and PSNR/MSE log files 
#The following Python code was used to automate the generation of 15 MP4 Video streams from the coastguard-original.mp4 and then to generate 15 Log files each containing 2400 data entries detailing the PSNR/MSE for each frame.  This can be run from a single python file.

Import os
Import subprocess

#change to C:\ucl-ims\video-files
os.chdir('/ucl-ims/video-files')	


#H265 Codec
os.chdir('/ucl-ims/h264-video-files')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libx264 -b:v 16k coastguard-16k.mp4 2> coastguard-16k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libx264 -b:v 128k coastguard-128k.mp4 2> coastguard-128k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libx264 -b:v 512k coastguard-512k.mp4 2> coastguard-512k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libx264 -b:v 1024k coastguard-1024k.mp4 2> coastguard-1024k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libx264 -b:v 2048k coastguard-2048k.mp4 2> coastguard-2048k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-16k.mp4 -lavfi  psnr="stats_file=coastguard-16k-psnr.log" -f null -
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-128k.mp4 -lavfi  psnr="stats_file=coastguard-128k-psnr.log" -f null -
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-512k.mp4 -lavfi  psnr="stats_file=coastguard-512k-psnr.log" -f null -
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-1024k.mp4 -lavfi  psnr="stats_file=coastguard-1024k-psnr.log" -f null -
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-2048k.mp4 -lavfi  psnr="stats_file=coastguard-2048k-psnr.log" -f null -

#H265 Codec
os.chdir('/ucl-ims/h266-video-files')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libx265 -b:v 16k coastguard-16k.mp4 2> coastguard-16k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libx265 -b:v 128k coastguard-128k.mp4 2> coastguard-128k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libx265 -b:v 512k coastguard-512k.mp4 2> coastguard-512k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libx265 -b:v 1024k coastguard-1024k.mp4 2> coastguard-1024k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libx265 -b:v 2048k coastguard-2048k.mp4 2> coastguard-2048k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-16k.mp4 -lavfi  psnr="stats_file=coastguard-16k-psnr.log" -f null -')
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-128k.mp4 -lavfi  psnr="stats_file=coastguard-128k-psnr.log" -f null -')
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-512k.mp4 -lavfi  psnr="stats_file=coastguard-512k-psnr.log" -f null -')
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-1024k.mp4 -lavfi  psnr="stats_file=coastguard-1024k-psnr.log" -f null -')
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-2048k.mp4 -lavfi  psnr="stats_file=coastguard-2048k-psnr.log" -f null -')

#VP9 Codec 
os.chdir('/ucl-ims/h266-video-files')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libvpx-vp9 -b:v 16k coastguard-16k.webm 2> coastguard-16k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libvpx-vp9 -b:v 128k coastguard-128k.webm 2> coastguard-128k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libvpx-vp9 -b:v 512k coastguard-512k.webm 2> coastguard-512k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libvpx-vp9 -b:v 1024k coastguard-1024k.webm 2> coastguard-1024k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -c:v libvpx-vp9 -b:v 2048k coastguard-2048k.webm 2> coastguard-2048k.txt')
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-16k.webm -lavfi  psnr="stats_file=coastguard-16k-psnr.log" -f null -
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-128k.webm -lavfi  psnr="stats_file=coastguard-128k-psnr.log" -f null -')
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-512k.webm -lavfi  psnr="stats_file=coastguard-512k-psnr.log" -f null -')
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-1024k.webm -lavfi  psnr="stats_file=coastguard-1024k-psnr.log" -f null –')
os.popen('ffmpeg -i coastguard-original.mp4 -i coastguard-2048k.webm -lavfi  psnr="stats_file=coastguard-2048k-psnr.log" -f null -')


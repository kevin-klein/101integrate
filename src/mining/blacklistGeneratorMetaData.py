import sys
import constants
import simplejson as json
import logging #needed for nunning the whole project in debug/info-mode
import logging.config
import copy

##
# @param	args	the resource from which to retrieve the blacklisted chapters
def generateBlacklist(args):
	for a in args:
		blacklist =[]
		path = constants.getMetaPath(a)
		try:
		    blacklist = json.loads(open(path+"blacklist.json" , 'rb').read())
		except IOError:
		    pass
		else:
		    print "loaded old blacklist"
		try:
			chapters = json.loads(open(path + "chapterData.json", 'rb').read())['chapters']
			usedChapters =  json.loads(open(path + "chapters.json", 'rb').read())['chapters']
			notInTxt = copy.copy(chapters)
			for c in chapters:
				for l in open(path  + "chapters.txt").readlines():
					if c['url'] == l.strip():
						notInTxt.remove(c)
			notInJSON = copy.copy(chapters)
			for c in chapters:
				for u in usedChapters:
					if u['file'] == c['file'] and u['title'] in c['title']:
						notInJSON.remove(c) 
			newBlacklist= [json.loads(b) for b in set([json.dumps(b) for b in (notInTxt + notInJSON)])]# remove duplicates
			print newBlacklist
			print "generated Blacklist"
			for b in newBlacklist:
				b['reason'] = ""
			# Keep reasons
			if blacklist:
			    print "copying reasons"
			for b in blacklist:
			    for n in newBlacklist:
				if b['url'] == n['url']:
				    n['reason']=b['reason']
			blacklist = newBlacklist
		except IOError, e:
			print e
			print "Could not read "+a+"-Files \r\n Try running MetadataGenerator before BlacklistGenerator"
		else:
			pass
		WriteJSON = open(path+"blacklist.json","w")
		WriteJSON.write(json.dumps(blacklist, indent="\t"))
		WriteJSON.close()
		print "Wrote File"

if __name__ == "__main__":
	logging.config.fileConfig('../config/pythonLogging.conf')
	generateBlacklist(sys.argv[1:])

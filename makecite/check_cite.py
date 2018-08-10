"""makecite.check_cite.py: check in .tex file if all packages mentioned are also cited
"""
# Standard libraries
import os
import json

# Package
from .cmdline import get_bibtex

_bib_path = os.path.join(os.path.split(os.path.abspath(__file__))[0],'bibfiles')

####
# helper functions

#check if package A is in current line
def is_package_in_line(package,line):
    return package.lower() in line.lower()

#check if references B are in current line
def are_references_in_line(references,line):
    if len(references) == 0:  #the reference was not found in the bibtex
        return False
    return all([ref.lower() in line.lower() for ref in references])


def notify_package_referenced(package,reference):
    print('[\033[1m\033[92m  OK   \033[0m]: package \033[1m{}\033[0m mentioned and referenced'.format(package))

def notify_package_not_referenced(package,reference):
    print('[\033[1m\033[91mWARNING\033[0m]: package \033[1m{}\033[0m mentioned but not referenced'.format(package))





def get_citekey_from_bibtex(package_name,bibtex_filename):
    """For a package found in the .tex file, fetch the cite_key from the .bib file
       NOTE: .bib file should  be the one used to compile the .tex file
    
    Parameters
    ----------
    package_name: str
    bibtex_filename: str
    
    
    Returns
    -------
    cite_keys: list
    
    """
    
    try:
        bibtex = get_bibtex(package_name)
        bibtex_entries = bibtex.split('@')[1:]
    except ValueError:
        # Package doesn't have a .bib file in this repo.
        return None
        
    #parse the entry in the library and return (all) titles of corresponding articles
    article_titles = []
    for entry in bibtex_entries:
        for line in entry:
            if 'title' in line.lower():
                title = line.split('=')[1].replace('"','').replace('{','').replace('}','').strip(' ')
                article_titles.append(title)
                break
    
    #print(article_titles)
    #in the bibtex file, find the reference corresponding to the titles
    cite_keys = []
    for title in article_titles:            
        with open(bibtex_filename,'r') as f:
            for entry in f.readlines():
                if title.lower() in entry.lower(): 
                    #this is the reference we are looking for
                    cite_key = entry.split(',')[0].split('{')[1]
                    cite_keys.append(cite_key)
                    break

    return cite_keys
    
  
def 
    
    
def main(tex_filename,bibtex_filename):
    #texfile = os.path.join('.', 'sometexfile.tex')
    #bibtexfile = os.path.join('.','somebibfile.bib')
    libraryfile = os.path.join('makecite','makecite','modules.json')
    with open(libraryfile) as f:
        library = json.load(f)
    
    
    
    with open(texfile,'r') as texfile:
    for line in texfile.readlines():
        if line.startswith('%'):  #this line is commented out in latex
            continue
        
        for package_name in library.keys():
            if is_package_in_line(package,line):     
                #software package is used
                cite_keys = get_citekey_from_library(package_name,bibtex_filename)
                
                #is the package also reference: Y/N
                if are_references_in_line(reference,line):   #if Yes
                    notify_package_referenced(package,reference)
                else:                                      #if No    
                    notify_package_not_referenced(package,reference)
    




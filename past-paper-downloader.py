from requests import get
from winsound import Beep
from os.path import exists, join
from os import mkdir


def beep(error=False):
    Beep(250 if error else 500 ,500)
    
def download_pdf(url, dest, name):
    try:
        if exists(join(dest,name)):
            print("[+] File Already Exists")
            beep()
            beep()
            return

        print(f"[+] Downloading {url}")
        res = get(url)
        res.raise_for_status()

        with open(join(dest,name), "wb") as file:
                  file.write(res.content)
        beep()
        print(f"[+] Download Successful")
    
    except Exception as e:
        beep(True)
        print(f"[-] Download Unsuccessful: {e}")
    

if __name__ == "__main__":
    # Dictionary mapping subjects to their exam codes and paper variants
    subjects = {"Biology%20(0610)":('0610', 22, 42, 62),
                "Physics%20(0625)":('0625', 22, 42, 62),
                "Chemistry%20(0620)":('0620', 22, 42, 62),
                "Economics%20(0455)":('0455', 12,22),
                "English%20-%20First%20Language%20(0500)":('0500', 12, 22),
                "Mathematics%20(0580)":('0580', 21, 41),
                "Geography%20(0460)":('0460', 12, 22, 42),
                "Computer%20Science%20(0478)":('0478', 12, 22)}

    # Base URL for downloading the past papers
    base_url = "https://papers.xtremepape.rs/CAIE/IGCSE/{}/{}_{}{}_{}_{}.pdf"

    # Range of years for which papers are to be downloaded (2016-2022)
    years = range(16, 23)

    # Exam seasons: Winter (w), Summer (s), March (m)
    exam_seasons = "wsm"

    # Parent directory where all papers will be saved
    parent_dir = "Past Papers"
    
    for subject in subjects:
        # Create a directory for each subject
        _dir = join(parent_dir,subject.split("%20")[0])
        if not exists(_dir): mkdir(_dir)
        exam_code, *variants = subjects[subject]

        for year in years:
            # Create a directory for each year
            child_dir = join(_dir, f"20{str(year)}")
            if not exists(child_dir): 
                mkdir(child_dir)

            for variant in variants:
                for season in exam_seasons:
                    # Construct and download the question paper
                    qp = base_url.format(subject, exam_code, season, year, "qp", variant)
                    qp_name = qp.split("/")[-1]
                    download_pdf(qp, child_dir, qp_name)
                    
                    # Construct and download the marking scheme
                    ms = base_url.format(subject, exam_code, season, year, "ms", variant)
                    ms_name = ms.split("/")[-1]
                    download_pdf(ms, child_dir, ms_name)

class Naming():
    # dunderscore = double score
    def __init__(self) -> None:
        self._weak_private = "WEAK"
        self.__strong_private = "STRONG"
        self.public = "PUBLIC"


if __name__ == "__main__":
    naming = Naming()
    print("===== Public Attribute =====")
    print(naming.public, end="\n\n")

    print("===== Weak Private Attribute =====")
    print(naming._weak_private, end="\n\n")
    
    try:
        print(naming.__strong_private, end="\n\n")
    except AttributeError as err:
        print("===== Error Message =====")
        print(err, end="\n\n")

    print("===== Strong Private Attribute Naming Mangling =====")
    print(naming._Naming__strong_private, end="\n\n")
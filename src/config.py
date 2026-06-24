CHUNK_SIZE = 300

CHUNK_OVERLAP = 50

TOP_K_RESULTS = 3

GEMINI_MAX_RETRIES = 3

GEMINI_RETRY_BASE_DELAY = 1

COLLECTION_NAME = "support_kb"

CHROMA_DB_PATH = "chroma_db"

GENERATION_MODEL = "gemini-2.5-flash"

EMBEDDING_MODEL = "gemini-embedding-001"

ESCALATION_KEYWORDS = [
    "delete",
    "deleted",
    "account deletion",
    "close account",
    "data removal",
    "remove my data",
    "erase my data",
    "legal",
    "lawsuit",
    "court",
    "billing dispute",
    "refund dispute"
]
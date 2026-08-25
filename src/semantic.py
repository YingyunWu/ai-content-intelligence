from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the embedding model once.
# The model is cached locally after the first download.
MODEL = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def compute_topic_similarity(
    topics: list[str]
) -> list[list[float]]:
    """
    Compute pairwise semantic similarity between topics.

    Args:
        topics: A list of topic strings.

    Returns:
        A similarity matrix represented as a list of lists.
    """

    if not topics:
        return []

    embeddings = MODEL.encode(
        topics,
        convert_to_numpy=True
    )

    similarity_matrix = cosine_similarity(
        embeddings
    )

    return similarity_matrix.tolist()


def group_similar_topics(
    topics: list[str],
    threshold: float = 0.70
) -> list[list[str]]:
    """
    Group semantically similar topics using a strict
    representative-based similarity rule.

    A topic is added to an existing group only when its
    similarity with the group's representative topic
    is greater than or equal to the threshold.

    Args:
        topics: A list of topic strings.
        threshold: Similarity threshold between 0 and 1.

    Returns:
        A list of topic groups.
    """

    if not topics:
        return []

    similarity_matrix = compute_topic_similarity(
        topics
    )

    groups = []

    # Store the index of the representative topic
    # for each group.
    representatives = []

    for i, topic in enumerate(topics):

        assigned = False

        # Compare the current topic with each
        # existing group's representative.
        for group_index, representative_index in enumerate(
            representatives
        ):

            similarity = similarity_matrix[
                i
            ][
                representative_index
            ]

            if similarity >= threshold:

                groups[group_index].append(
                    topic
                )

                assigned = True

                break

        # If the topic does not match any existing
        # representative, create a new group.
        if not assigned:

            groups.append(
                [topic]
            )

            representatives.append(
                i
            )

    return groups


def get_representative_topic(
    topic_group: list[str]
) -> str:
    """
    Select the most representative topic from a
    semantic topic group.

    The topic with the highest average semantic
    similarity to the other topics is selected.

    Args:
        topic_group: A list of semantically related topics.

    Returns:
        The most representative topic.
    """

    if not topic_group:
        return ""

    if len(topic_group) == 1:
        return topic_group[0]

    similarity_matrix = compute_topic_similarity(
        topic_group
    )

    best_index = 0
    best_score = -1

    for i, row in enumerate(
        similarity_matrix
    ):

        similarities = [
            score
            for j, score in enumerate(row)
            if i != j
        ]

        average_similarity = (
            sum(similarities)
            / len(similarities)
        )

        if average_similarity > best_score:

            best_score = average_similarity
            best_index = i

    return topic_group[best_index]
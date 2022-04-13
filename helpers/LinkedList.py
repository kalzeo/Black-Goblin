from pathlib import Path

import pandas as pd
from helpers.Frame import Frame


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, **kwargs):
        """
        Insert content to the beginning of the linked list
        :param kwargs: The contents to add i.e. frame, object, id, and timestamp
        """
        node = Frame(**kwargs)
        node.next = self.head
        self.head = node

    def append(self, **kwargs):
        """
        Insert content to the end of the linked list
        :param kwargs: The contents to add i.e. frame, object, id, and timestamp
        """
        node = Frame(**kwargs)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def __iter__(self):
        """
        Returns an iterator generator that yields nodes in the linked list
        """
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def ll2csv(self, df: pd.DataFrame, save_dir: Path):
        """
        Store the contents of the linked list in a CSV file. The contents will be grouped accordingly to only
        display the timestamps of when an object comes in and out of frame.
        :param save_dir: The directory to where the CSV file will be saved
        :param df: An empty dataframe to store the contents of the linked list
        """
        MAX_FRAMES_BEFORE_DISCARD = 1

        for c in self:
            temp = c
            frame, obj, obj_id, timestamp_in, timestamp_out = c.frame, c.obj, c.id, c.timestamp, c.timestamp

            last_seen = frame
            while temp is not None:
                if c.obj == temp.obj and c.id == temp.id and temp.frame - last_seen <= MAX_FRAMES_BEFORE_DISCARD:
                    timestamp_out = temp.timestamp
                    last_seen = temp.frame
                temp = temp.next

            _df = df.loc[
                (df["Object"] == obj) & (df["ID"] == obj_id) & (df["Timestamp_Out"] == timestamp_out)]

            if len(_df) == 0:
                df.loc[len(df) + 1] = [frame, obj, obj_id, timestamp_in, timestamp_out]

        df.drop(columns=["Frame"], inplace=True)
        df.to_csv(save_dir.as_posix(), index=False)

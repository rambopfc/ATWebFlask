class Notes:

    def __init__(self, notes):
        if 'Description' in notes:
            self.Description = notes['Description']
        else:
            self.Description = ""

        if 'NoteType' in notes:
            self.NoteTypeID = notes['NoteType']
        else:
            self.NoteType = ""

        if 'NoteType' in notes:
            noteint = notes['NoteType']
            if noteint == 2:
                self.NoteType = "Task Detail"
            if noteint == 3:
                self.NoteType = "Task Notes"
            if noteint == 1:
                self.NoteType = "Task Summary"
            else:
                self.NoteType = ""
        else:
            self.NoteType = ""

        if 'Publish' in notes:
            self.PublishID = notes['Publish']
        else:
            self.PublishID = ""

        if 'Publish' in notes:
            pubint = notes["Publish"]
            if pubint == 1:
                self.Publish = "All Autotask Users"
            if pubint == 2:
                self.Publish = "Internal Users Only"
        else:
            self.Publish = ""

        if 'id' in notes:
            self.ID = notes['id']
        else:
            self.ID = ""

        if 'LastActivityDate' in notes:
            self.Date = notes['LastActivityDate']
        else:
            self.Date = ""

        if 'Title' in notes:
            self.Title = notes['Title']
        else:
            self.Title = ""

        if 'TicketID' in notes:
            self.TicketID = notes['TicketID']
        else:
            self.TicketID = ""
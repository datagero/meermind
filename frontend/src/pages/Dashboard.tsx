import { Container } from '@mui/material';
import ResponsiveGrid from '../components/ResponsiveGrid';
import React, { useEffect } from 'react';
import { Note } from "../types/Note"; // Update the path to the correct location of the 'Note' type file
import { NotesAPI } from '../api/NotesAPI';
import SearchBar from '../components/SearchBar';
import { app } from '../api/configs/realmConfig';
import * as Realm from "realm-web";
interface Props {
  // Define your component props here
}

export interface NoteData {
  transcript_summary: Note,
  id: string
}
const Dashboard: React.FC<Props> = () => {
  // Add your component logic here

  const [notes, setNotes] = React.useState<NoteData[]>([])
  const [comments, setComments] = React.useState<any[]>([])
  const [searchText, setSearchText] = React.useState<any>(null)
  useEffect(() => {
    if (searchText == null) {
      NotesAPI.getAll().then((notes: any) => {
        const filteredNotes: NoteData[] = notes.data.map((note: any) => ({

          transcript_summary: note.transcript_summary,
          id: note.document_hash_id
        }));
        setNotes(filteredNotes)
      })
    }
    else {
      NotesAPI.search(searchText).then((notes: any) => {
        console.log(notes)
        const filteredNotes: NoteData[] = notes.data.map((note: any) => ({
          transcript_summary: note.transcript_summary,
          id: note.document_hash_id
        }));
        setNotes(filteredNotes)
      })
    }
  }, [searchText])


  return (
    <div>
      <Container maxWidth="lg">
        <h1>Your Notes</h1>
        <SearchBar setSearchText={setSearchText} />
        <ResponsiveGrid notes={notes || []} />
      </Container>
    </div>
  );
};

export default Dashboard;

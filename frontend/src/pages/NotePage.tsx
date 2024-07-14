import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import type { Note , StudentSummary} from '../types/Note';
import { NotesAPI } from '../api/NotesAPI';
import { Container } from '@mui/material';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';

const NotePage: React.FC = () => {

    const { id } = useParams() ?? { id: '' };
    const [note, setNote] = React.useState<Note | null>(null);

    useEffect(() => {
        NotesAPI.getNote(id as string).then((note: any) => {
            setNote(note.data.transcript_summary)
        })
    }, [id])
    return (
        <Container maxWidth="md">
        <Box
            sx={{
            display: 'flex',
            flexWrap: 'wrap',
            alignItems: 'center',
            justifyContent: 'center',
            '& > :not(style)': {
                m: 3,
                p: 5,
                width: 400,
            },
            }}
        >
        <Paper elevation={3} >
            <h1>{note?.title}</h1>
            <h3>{note?.oneLineSummary}</h3>
            </Paper>
            { note?.studentSummary.map((summary: StudentSummary) => ( 
                <Paper elevation={3} key={summary.summaryTitle}>
                    <h3>{summary.summaryTitle}</h3>
                    {summary.summaryPoints.map((point: string) => (<li>{point}</li>))}
                </Paper>
            ))}
        </Box>
        </Container>
    );
};

export default NotePage;
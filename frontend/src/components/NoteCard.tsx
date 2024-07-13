import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
// Import the 'Note' type from the correct file path
import { Note } from '../types/Note'

const bull = (
  <Box
    component="span"
    sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
  >
    •
  </Box>
);


export default function NoteCard({ note }: { note: Note }) {
  return (
    <Box sx={{ minWidth: 275 }}>
      <Card variant="outlined" sx={{ height: 300}}>
        <CardContent>
            <Typography sx={{ fontSize: 24 }} color="text.primary" gutterBottom>
                {note.title}
            </Typography>
            <Typography sx={{ mb: 1.5 }} color="text.secondary">
                {note.oneLineSummary}
            </Typography>
            {/* <Typography variant="body2">
                well meaning and kindly.
                <br />
                {'"a benevolent smile"'}
            </Typography> */}
        </CardContent>
        <CardActions>
            <Button size="small">Learn More</Button>
        </CardActions>
      </Card>
    </Box>
  );
}
